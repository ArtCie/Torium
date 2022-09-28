from endpoints.members.db_manager import DBManager
from endpoints.members.content import ContentConverter


class PostMember:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs, status='pending')

    def process_request(self):
        self._post_group()

    def _post_group(self):
        data = {
            "group_id": self._content.group_id,
            "user_id": self._content.user_id,
            "status": self._content.status,
            "timestamp": self._content.timestamp
        }
        self._db_manager.post_member(data)
