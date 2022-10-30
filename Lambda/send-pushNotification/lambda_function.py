from secret_manager import SecretManager
import logging
from json import loads

from send_push_notification_manager import SendPushNotificationManager
from db_manager import DBManager


def lambda_handler(event: dict, context: dict) -> dict:
    content = loads(event['Records'][0]['body'])
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info(f"{event=} {context=}")

    secret_manager = SecretManager()
    db_config = secret_manager.get_db_config()
    db_manager = DBManager(db_config)
    db_manager.connect()

    send_push_notification_manager = SendPushNotificationManager(db_manager, content)
    return send_push_notification_manager.process()
