import random
import string

from endpoints.users.db_manager import DBManager
from endpoints.users.content import ContentConverter
from aws.sns_manager import SnsManager


class PostUserMobile:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs)
        self._sns_manager = SnsManager()

    def process_request(self):
        code = self._generate_code()
        self._init_phone_update(code)
        self._send_sms(code)

    def _init_phone_update(self, code: str):
        data = {
            "user_id": self._content.user_id,
            "code": code,
            "is_sent": True,
            "is_confirmed": False,
            "mobile_number": self._content.mobile_number,
            "timestamp": self._content.timestamp
        }
        self._db_manager.init_phone_number(data)

    @staticmethod
    def _generate_code():
        return ''.join(random.choice(string.digits) for _ in range(6))

    def _send_sms(self, code):
        message = self._generate_message(code)
        self._sns_manager.send_message(self._content.mobile_number, message)

    @staticmethod
    def _generate_message(code):
        return f"Your verification code is: {code}"
