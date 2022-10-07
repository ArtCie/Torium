from logger import log
from utils import log_exception, build_response

from db_manager import DBManager

from datetime import datetime
from sqs_manager import SqsManager
from event_builder import EventBuilder, Event
import json

class ScheduleEventsManager:
    @log
    def __init__(self, db_manager: DBManager):
        self._db_manager = db_manager
        self.s3_manager = SqsManager()

    @log
    def process(self) -> dict:
        try:
            self._handle_event()
            self._db_manager.commit_changes()
            return self._build_response('OK', 200)
        except Exception as e:
            log_exception(type(self).__name__, str(e))
            self._db_manager.rollback_changes()
            return self._build_response(str(e), 500)
        finally:
            self._db_manager.close_cursor()
            self._db_manager.close_connection()

    def _handle_event(self):
        events = self._select_events()
        self._process_event(events)

    def _select_events(self) -> list:
        data = {
            "timestamp": datetime.utcnow()
        }
        result = self._db_manager.select_events(data)
        return EventBuilder.build_events(result)

    @log
    def _process_event(self, events) -> None:
        for event in events:
            message = self._build_message(event)
            self.s3_manager.create_sqs_schedule_notifications_event(message)

    @staticmethod
    def _build_message(event) -> dict:
        return {
            "event_id": {
                "DataType": "String",
                "StringValue": str(event.id)
            }
        }

    @staticmethod
    def _build_response(message: str, response_code: int) -> dict:
        return {
            'statusCode': response_code,
            'body': json.dumps(message)
        }