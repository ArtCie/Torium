from endpoints.events.db_manager import DBManager
from endpoints.exceptions import AccessDenied


class DeleteEvent:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._id = kwargs["id"]
        self._user_id = kwargs["user_id"]

    def process_request(self):
        self._valid_user_event_relation()
        self._delete_event_users()
        self._delete_event()

    def _valid_user_event_relation(self):
        data = {
            "user_id": self._user_id,
            "event_id": self._id
        }
        if not self._db_manager.valid_user_event_relation(data):
            raise AccessDenied("Access Denied!")

    def _delete_event_users(self):
        data = {
            "event_id": self._id
        }
        self._db_manager.delete_event_users(data)

    def _delete_event(self):
        data = {
            "event_id": self._id
        }
        self._db_manager.delete_event(data)