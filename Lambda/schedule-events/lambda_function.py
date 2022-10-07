from secret_manager import SecretManager
import logging

from schedule_events_manager import ScheduleEventsManager
from db_manager import DBManager


def lambda_handler(event: dict, context: dict) -> dict:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info(f"{event=} {context=}")

    secret_manager = SecretManager()
    db_config = secret_manager.get_db_config()
    db_manager = DBManager(db_config)
    db_manager.connect()

    pre_signup_manager = ScheduleEventsManager(db_manager)
    return pre_signup_manager.process()
