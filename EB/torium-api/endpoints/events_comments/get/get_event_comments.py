from endpoints.events_comments.db_manager import DBManager
from endpoints.events_comments.content import ContentConverter
from utils.object_builder import ObjectBuilder


class GetEventComments:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._event_id = kwargs["event_id"]

    def process_request(self) -> dict:
        event_comments = self._get_event_comments()
        parsed_event_comments = self._parse_event_comments(event_comments)
        return ObjectBuilder.build_object(parsed_event_comments)

    def _get_event_comments(self) -> list:
        data = {
            "event_id": self._event_id
        }
        return self._db_manager.get_events_comments(data)

    @staticmethod
    def _parse_event_comments(groups: list) -> list:
        return [ContentConverter.convert(row) for row in groups]
