from endpoints.events_comments.db_manager import DBManager
from endpoints.events_comments.content import ContentConverter
from endpoints.exceptions import AccessDenied


class PutEventComment:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs)

    def process_request(self):
        self._valid_user_event_relation()
        self._update_event_comment()

    def _valid_user_event_relation(self):
        data = {
            "user_id": self._content.user_id,
            "id": self._content.id
        }
        if not self._db_manager.valid_user_comment_relation(data):
            raise AccessDenied("Access Denied!")

    def _update_event_comment(self):
        data = {
            "id": self._content.id,
            "comment": self._content.comment
        }
        return self._db_manager.update_event_comment(data)

