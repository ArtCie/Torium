from secret_manager import SecretManager
import logging
from json import loads

from schedule_notifications_manager import ScheduleNotificationsManager
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

    schedule_events_manager = ScheduleNotificationsManager(db_manager, content)
    return schedule_events_manager.process()
