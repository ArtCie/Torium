from endpoints.groups.db_manager import DBManager
from endpoints.groups.content import ContentConverter
from endpoints.groups.exceptions import AccessDenied


class DeleteGroup:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self.content = ContentConverter.convert_delete(kwargs)

    def process_request(self):
        self._valid_permission()
        self._delete_group_associations()
        self._delete_group()

    def _valid_permission(self):
        data = {
            "admin_id": self.content.admin_id,
            "group_id": self.content.group_id
        }
        if not self._db_manager.valid_permission(data):
            raise AccessDenied("Access Denied!")

    def _delete_group_associations(self):
        data = {
            "group_id": self.content.group_id
        }
        self._db_manager.delete_events(data)
        self._db_manager.delete_users_group(data)
        self._db_manager.delete_group_invitation_logs(data)

    def _delete_group(self):
        data = {
            "id": self.content.group_id
        }
        self._db_manager.delete_group(data)
