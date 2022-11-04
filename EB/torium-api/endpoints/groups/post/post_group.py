from endpoints.groups.db_manager import DBManager
from endpoints.groups.content import ContentConverter


class PostGroup:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert_post(kwargs)
        self.STATUS = "admin"

    def process_request(self):
        group_id = self._post_group()
        self._insert_users_groups(group_id)
        return {
            "group_id": group_id
        }

    def _post_group(self):
        data = {
            "name": self._content.name,
            "description": self._content.description,
            "admin_id": self._content.admin_id,
            "timestamp": self._content.timestamp
        }
        return self._db_manager.post_group(data)[0]

    def _insert_users_groups(self, group_id: int):
        data = {
            "user_id": self._content.admin_id,
            "group_id": group_id,
            "status": self.STATUS,
            "timestamp": self._content.timestamp
        }
        self._db_manager.insert_users_groups(data)