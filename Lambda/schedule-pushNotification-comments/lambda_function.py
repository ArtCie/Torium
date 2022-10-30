from secret_manager import SecretManager
import logging
from json import loads

from schedule_push_notification_comments_manager import SchedulePushNotificationCommentsManager
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

    schedule_push_notification_comments_manager = SchedulePushNotificationCommentsManager(db_manager, content)
    return schedule_push_notification_comments_manager.process()
