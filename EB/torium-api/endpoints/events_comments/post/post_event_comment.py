from endpoints.events_comments.db_manager import DBManager
from endpoints.events_comments.content import ContentConverter
from endpoints.exceptions import AccessDenied


class PostEventComment:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs)

    def process_request(self):
        self._valid_user_event_relation()
        self._post_event_comment()

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

