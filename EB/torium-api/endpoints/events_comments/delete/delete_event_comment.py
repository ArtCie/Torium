from endpoints.events_comments.db_manager import DBManager
from endpoints.exceptions import AccessDenied


class DeleteEventComment:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._id = kwargs["id"]
        self._user_id = kwargs["user_id"]

    def process_request(self):
        self._delete_event_comment()

    def _delete_event_comment(self):
        data = {
            "id": self._id,
            "user_id": self._user_id
        }
        if not self._db_manager.delete_event_comment(data):
            raise AccessDenied("Access Denied!")
