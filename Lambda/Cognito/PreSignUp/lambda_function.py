from secret_manager import SecretManager
import logging

from pre_sign_up_manager import PreSignUpManager
from resources.content import ContentConverter
from db_manager import DBManager


def lambda_handler(event: dict, context: dict) -> dict:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info(f"{event=} {context=}")

    user_attributes = ContentConverter.convert(event)

    secret_manager = SecretManager()
    db_config = secret_manager.get_db_config()
    db_manager = DBManager(db_config)
    db_manager.connect()

    pre_signup_manager = PreSignUpManager(db_manager, user_attributes)
    pre_signup_manager.process()
    return event
