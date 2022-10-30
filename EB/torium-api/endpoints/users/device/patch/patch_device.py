from endpoints.users.db_manager import DBManager
from aws.sns_manager import SnsManager


class PatchDevice:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._sns_manager = SnsManager()
        self._user_id = kwargs["user_id"]
        self._device_token = kwargs["device_token"]

    def process_request(self):
        current_arn, current_device_token = self._select_current_device_data()
        if not current_device_token:
            sns_arn = self._sns_manager.add_endpoint(self._user_id, self._device_token)
            self._update_device_data(sns_arn)
        else:
            self._sns_manager.update_token_in_sns_endpoint(self._user_id, current_arn, self._device_token)
            self._update_device_token()

    def _select_current_device_data(self):
        data = {
            "user_id": self._user_id,
        }
        return self._db_manager.select_current_device_data(data)

    def _update_device_data(self, sns_arn):
        data = {
            "device_arn": sns_arn,
            "device_token": self._device_token,
            "user_id": self._user_id
        }
        self._db_manager.update_device_data(data)

    def _update_device_token(self):
        data = {
            "user_id": self._user_id,
            "device_token": self._device_token
        }
        self._db_manager.update_device_token(data)
