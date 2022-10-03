from endpoints.users.db_manager import DBManager
from endpoints.users.content import ContentConverter
from utils.object_builder import ObjectBuilder


class GetUser:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]

    def process_request(self) -> dict:
        user = self._get_user()
        parsed_user = self._parse_user([user])
        return ObjectBuilder.build_object(parsed_user)[0]

    def _get_user(self) -> dict:
        data = {
            "user_id": self._user_id
        }
        return self._db_manager.get_user(data)

    @staticmethod
    def _parse_user(groups: list) -> list:
        return [ContentConverter.convert(row) for row in groups]
