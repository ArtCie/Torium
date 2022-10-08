from secret_manager import SecretManager
import logging
from json import loads

from send_sms_manager import SendSmsManager
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

    send_sms_manager = SendSmsManager(db_manager, content)
    return send_sms_manager.process()
