from endpoints.events.db_manager import DBManager
from endpoints.events.content import ContentConverter
from endpoints.exceptions import AccessDenied

from psycopg2.extras import DictRow


class PutEvent:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]
        self._content = ContentConverter.convert(kwargs)

    def process_request(self):
        self._valid_user_event_relation()
        self._update_event()
        self._update_users_event()

    def _valid_user_event_relation(self):
        data = {
            "user_id": self._user_id,
            "event_id": self._content.id
        }
        if not self._db_manager.valid_user_event_relation(data):
            raise AccessDenied("Access Denied!")

    def _update_event(self):
        data = {
            "id": self._content.id,
            "is_budget": self._content.is_budget,
            "budget": self._content.budget,
            "description": self._content.description,
            "group_id": self._content.group_id,
            "event_timestamp": self._content.event_timestamp,
            "reminder": self._content.reminder,
            "schedule_period": self._content.schedule_period,
            "timestamp": self._content.timestamp
        }
        return self._db_manager.update_event(data)

    def _update_users_event(self):
        current_users = self._select_event_users()
        self._insert_event_users(current_users)
        self._delete_event_users(current_users)

    def _select_event_users(self):
        data = {
            "id": self._content.id
        }
        return self._db_manager.select_event_users(data)[0]

    def _insert_event_users(self, current_users: DictRow):
        users_to_insert = set(self._content.users) - set(list(current_users))
        for user_id in users_to_insert:
            self._insert_event_user(user_id)

    def _insert_event_user(self, user_id: int):
        data = {
            "user_id": user_id,
            "event_id": self._content.id,
            "timestamp": self._content.timestamp
        }
        self._db_manager.insert_event_user(data)

    def _delete_event_users(self, current_users: DictRow):
        users_to_remove = set(current_users) - set(list(self._content.users))
        for user_id in users_to_remove:
            self._delete_event_user(user_id)

    def _delete_event_user(self, user_id: int):
        data = {
            "user_id": user_id,
            "event_id": self._content.id
        }
        self._db_manager.delete_event_user(data)