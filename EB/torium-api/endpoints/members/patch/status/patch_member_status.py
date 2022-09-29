from endpoints.members.db_manager import DBManager
from endpoints.members.content import ContentConverter


class PatchMemberStatus:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs, status=kwargs["status"])
        self.STATUS = "standard"

    def process_request(self):
        self._update_group_invitation_logs()
        if self._content.status == "confirmed":
            self._insert_users_groups()

    def _update_group_invitation_logs(self):
        data = {
            "group_id": self._content.group_id,
            "user_id": self._content.user_id,
            "status": self._content.status,
            "updated_timestamp": self._content.timestamp
        }
        self._db_manager.update_group_invitation_logs(data)

    def _insert_users_groups(self):
        data = {
            "group_id": self._content.group_id,
            "user_id": self._content.user_id,
            "status": self.STATUS,
            "timestamp": self._content.timestamp
        }
        self._db_manager.insert_users_groups(data)