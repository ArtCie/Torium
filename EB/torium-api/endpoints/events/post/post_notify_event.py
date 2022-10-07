from endpoints.events.db_manager import DBManager
from endpoints.exceptions import AccessDenied, LatencyError
from aws.sqs_manager import SqsManager


class PostNotifyEvent:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]
        self._event_id = kwargs["event_id"]
        self._sqs_manager = SqsManager()

    def process_request(self):
        self._valid_user_event_relation()
        self._valid_latency()
        self._send_notifications()

    def _valid_user_event_relation(self):
        data = {
            "user_id": self._user_id,
            "event_id": self._event_id
        }
        if not self._db_manager.valid_user_event_relation(data):
            raise AccessDenied("Access Denied!")

    def _valid_latency(self):
        data = {
            "event_id": self._event_id
        }
        if not self._db_manager.valid_latency(data):
            raise LatencyError("Event can be send once in 24 hours!")

    def _send_notifications(self):
        message = {
            "event_id": {
                "DataType": "String",
                "StringValue": str(self._event_id)
            }
        }
        self._sqs_manager.create_sqs_schedule_notifications_event(message)
