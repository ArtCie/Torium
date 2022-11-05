from endpoints.invitations.db_manager import DBManager


class GetInvitationsCount:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]
        self.STATUS = "sent"

    def process_request(self) -> dict:
        result = self._select_invitations_count()
        return {
            "count": result
        }

    def _select_invitations_count(self) -> list:
        data = {
            "user_id": self._user_id,
            "status": self.STATUS
        }
        return self._db_manager.select_invitations_count(data)[0]


