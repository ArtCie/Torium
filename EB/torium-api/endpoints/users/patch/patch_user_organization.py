from endpoints.users.db_manager import DBManager
from endpoints.users.content import ContentConverter


class PatchUserOrganization:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]
        self._content = ContentConverter.convert(kwargs)

    def process_request(self):
        self._update_user_organization()

    def _update_user_organization(self):
        data = {
            "user_id": self._user_id,
            "organization_id": self._content.organization_id
        }
        self._db_manager.update_user_organization(data)