from secret_manager import SecretManager
import logging

from post_sign_up_manager import PostSignUpManager
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

    post_signup_manager = PostSignUpManager(db_manager, user_attributes)
    post_signup_manager.process()
    return event
