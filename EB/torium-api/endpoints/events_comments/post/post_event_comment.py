from endpoints.events_comments.db_manager import DBManager
from endpoints.events_comments.content import ContentConverter
from endpoints.exceptions import AccessDenied
from aws.sqs_manager import SqsManager


class PostEventComment:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._sqs_manager = SqsManager()
        self._content = ContentConverter.convert(kwargs)

    def process_request(self):
        self._valid_user_event_relation()
        events_comments_id = self._post_event_comment()
        self._send_schedule_push_notification_comments_event(events_comments_id)

    def _valid_user_event_relation(self):
        data = {
            "user_id": self._content.user_id,
            "event_id": self._content.event_id
        }
        if not self._db_manager.valid_user_event_relation(data):
            raise AccessDenied("Access Denied!")

    def _post_event_comment(self):
        data = {
            "user_id": self._content.user_id,
            "event_id": self._content.event_id,
            "comment": self._content.comment,
            "timestamp": self._content.timestamp
        }
        return self._db_manager.post_event_comment(data)

    def _send_schedule_push_notification_comments_event(self, events_comments_id):
        message = {
            "events_comments_id": {
                "DataType": "String",
                "StringValue": str(events_comments_id)
            },
            "event_id": {
                "DataType": "String",
                "StringValue": str(self._content.event_id)
            },
            "event_timestamp": {
                "DataType": "String",
                "StringValue": str(self._content.timestamp)
            },
            "user_id": {
                "DataType": "String",
                "StringValue": str(self._content.user_id)
            },
            "comment": {
                "DataType": "String",
                "StringValue": str(self._content.comment)
            }
        }
        self._sqs_manager.create_sqs_schedule_push_notification_comments_event(message)

