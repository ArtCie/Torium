from endpoints.members.db_manager import DBManager
from endpoints.members.content import ContentConverter


class DeleteMember:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs)

    def process_request(self):
        self._delete_member()

    def _delete_member(self):
        data = {
            "group_id": self._content.group_id,
            "user_id": self._content.user_id,
        }
        self._db_manager.delete_member(data)
