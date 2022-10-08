from logger import log
from utils import log_exception, build_response

from db_manager import DBManager

from pinpoint_manager import PinpointManager
from content_builder import Content
import json


class SendEmailManager:
    @log
    def __init__(self, db_manager: DBManager, pinpoint_manager: PinpointManager, content: dict):
        self._db_manager = db_manager
        self._pinpoint_manager = pinpoint_manager
        self._content = Content(content)

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
        self._insert_event_reminders_logs()
        self._pinpoint_manager.create_send_email_event(self._content.email, self._content.message)

    @staticmethod
    def _build_response(message: str, response_code: int) -> dict:
        return {
            'statusCode': response_code,
            'body': json.dumps(message)
        }

    def _insert_event_reminders_logs(self):
        data = {
            "event_reminders_id": self._content.event_reminders_id,
            "send_timestamp": self._content.sent_timestamp,
            "user_id": self._content.user_id,
            "timestamp": self._content.timestamp
        }
        self._db_manager.insert_event_reminders_logs(data)

