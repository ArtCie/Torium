from endpoints.users.db_manager import DBManager
from endpoints.exceptions import WrongEmail


class GetUserIdByEmail:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._email = kwargs["email"]

    def process_request(self) -> dict:
        user_id = self._get_user()
        return self._valid_user_id(user_id)

    def _get_user(self) -> list:
        data = {
            "email": self._email
        }
        return self._db_manager.get_user_id_by_email(data)

    @staticmethod
    def _valid_user_id(user_id: list) -> dict:
        if not user_id:
            raise WrongEmail("Email is wrong!")
        return {
            "user_id": user_id[0]
        }