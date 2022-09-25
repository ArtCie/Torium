from endpoints.groups.db_manager import DBManager
from endpoints.groups.content import ContentConverter
from utils.object_builder import ObjectBuilder


class GetGroups:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]

    def process_request(self) -> dict:
        groups = self._get_groups()
        parsed_groups = self._parse_groups(groups)
        return ObjectBuilder.build_object(parsed_groups)

    def _get_groups(self) -> list:
        data = {
            "user_id": self._user_id
        }
        return self._db_manager.get_groups(data)

    @staticmethod
    def _parse_groups(groups: list) -> list:
        return [ContentConverter.convert(row) for row in groups]

