from endpoints.users.db_manager import DBManager
from endpoints.exceptions import WrongCode


class PatchUserPreferences:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._user_id = kwargs["user_id"]
        self._code = kwargs["code"]

    def process_request(self):
        mobile_number = self._confirm_code()
        self._update_user_mobile_number(mobile_number)

    def _confirm_code(self):
        data = {
            "user_id": self._user_id,
            "code": self._code
        }
        result = self._db_manager.confirm_code(data)
        if not result:
            return WrongCode("Given code is wrong!")
        return result[0]

    def _update_user_mobile_number(self, mobile_number: str):
        data = {
            "mobile_number": mobile_number,
            "user_id": self._user_id
        }
        self._db_manager.update_user_mobile_number(data)