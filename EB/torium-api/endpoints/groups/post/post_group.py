from endpoints.groups.db_manager import DBManager
from endpoints.groups.content import ContentConverter


class PostGroup:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert_post(kwargs)

    def process_request(self):
        self._post_group()

    def _post_group(self):
        data = {
            "name": self._content.name,
            "admin_id": self._content.admin_id,
            "timestamp": self._content.timestamp
        }
        self._db_manager.post_group(data)
