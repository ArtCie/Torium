from endpoints.members.db_manager import DBManager
from endpoints.members.content import ContentConverter
from utils.object_builder import ObjectBuilder


class GetMembers:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs)

    def process_request(self) -> dict:
        members = self._get_members()
        parsed_members = self._parse_members(members)
        return ObjectBuilder.build_object(parsed_members)

    def _get_members(self) -> list:
        data = {
            "user_id": self._content.user_id,
            "group_id": self._content.group_id
        }
        return self._db_manager.get_members(data)

    @staticmethod
    def _parse_members(groups: list) -> list:
        return [ContentConverter.convert_members(row) for row in groups]

