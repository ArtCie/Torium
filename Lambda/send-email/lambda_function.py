from secret_manager import SecretManager
import logging
from json import loads

from send_email_manager import SendEmailManager
from db_manager import DBManager
from pinpoint_manager import PinpointManager


def lambda_handler(event: dict, context: dict) -> dict:
    content = loads(event['Records'][0]['body'])
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info(f"{event=} {context=}")

    secret_manager = SecretManager()
    db_config = secret_manager.get_db_config()
    db_manager = DBManager(db_config)
    db_manager.connect()

    pinpoint_manager = PinpointManager(secret_manager)
    send_email_manager = SendEmailManager(db_manager, pinpoint_manager, content)
    return send_email_manager.process()
