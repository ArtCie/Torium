from endpoints.members.db_manager import DBManager
from endpoints.members.content import ContentConverter

from endpoints.exceptions import AccessDenied


class PatchMemberRole:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._admin_id = kwargs["admin_id"]
        self._content = ContentConverter.convert(kwargs, status=kwargs["status"])
        self.ADMIN = "admin"
        self.MODERATOR = "moderator"

    def process_request(self):
        self._valid_permissions()
        self._update_users_group()

    def _valid_permissions(self):
        if self._content.status == "admin":
            self._valid_admin_permissions()
        elif self._content.status == "moderator":
            self._valid_moderator_permissions()

    def _valid_admin_permissions(self):
        data = {
            "group_id": self._content.group_id,
            "admin_id": self._admin_id,
            "status": self.ADMIN
        }
        if not self._db_manager.valid_permissions(data):
            raise AccessDenied("Access Denied!")

    def _valid_moderator_permissions(self):
        data = {
            "group_id": self._content.group_id,
            "admin_id": self._admin_id,
            "status_moderator": self.MODERATOR,
            "status_admin": self.ADMIN,
        }
        if not self._db_manager.valid_moderator_permissions(data):
            raise AccessDenied("Access Denied!")

    def _update_users_group(self):
        data = {
            "group_id": self._content.group_id,
            "user_id": self._content.user_id,
            "status": self._content.status,
        }
        self._db_manager.update_users_group_status(data)