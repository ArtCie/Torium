from endpoints.events.db_manager import DBManager
from endpoints.events.content import ContentConverter
from utils.object_builder import ObjectBuilder


class GetEvents:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]
        self._group_id = kwargs.get("group_id")

    def process_request(self) -> dict:
        events = self._get_events()
        parsed_events = self._parse_events(events)
        return ObjectBuilder.build_object(parsed_events)

    def _get_events(self):
        if self._group_id:
            return self._get_user_group_events()
        else:
            return self._get_user_events()

    def _get_user_group_events(self) -> list:
        data = {
            "user_id": self._user_id,
        }
        return self._db_manager.get_user_group_events(data)

    def _get_user_events(self):
        data = {
            "user_id": self._user_id,
        }
        return self._db_manager.get_user_events(data)

    @staticmethod
    def _parse_events(groups: list) -> list:
        return [ContentConverter.convert(row) for row in groups]

