from endpoints.invitations.db_manager import DBManager
from endpoints.invitations.content import ContentConverter
from utils.object_builder import ObjectBuilder


class GetInvitations:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]
        self.STATUS = "sent"

    def process_request(self) -> dict:
        invitations = self._select_invitations()
        parsed_invitations = self._parse_invitations(invitations)
        return ObjectBuilder.build_object(parsed_invitations)

    def _select_invitations(self) -> list:
        data = {
            "user_id": self._user_id,
            "status": self.STATUS
        }
        return self._db_manager.select_invitations(data)

    @staticmethod
    def _parse_invitations(groups: list) -> list:
        return [ContentConverter.convert(row) for row in groups]

