from endpoints.events.db_manager import DBManager
from endpoints.events.content import ContentConverter


class PostEvent:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs)

    def process_request(self):
        event_id = self._post_event()
        self._insert_event_users(event_id)

    def _post_event(self):
        data = {
            "is_budget": self._content.is_budget,
            "budget": self._content.budget if self._content.is_budget else None,
            "description": self._content.description,
            "group_id": self._content.group_id,
            "event_timestamp": self._content.event_timestamp,
            "reminder": self._content.reminder,
            "schedule_period": self._content.schedule_period,
            "name": self._content.name,
            "timestamp": self._content.timestamp
        }
        return self._db_manager.post_event(data)[0]

    def _insert_event_users(self, event_id: int):
        for user_id in self._content.users:
            self._insert_event_user(user_id, event_id)

    def _insert_event_user(self, user_id: int, event_id: int):
        data = {
            "user_id": user_id,
            "event_id": event_id,
            "timestamp": self._content.timestamp
        }
        self._db_manager.insert_event_user(data)
