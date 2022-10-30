from typing import List


class User:
    def __init__(self, user_id: int, device_arn: str, email: str):
        self._user_id = user_id
        self._device_arn = device_arn
        self._email = email

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def device_arn(self) -> str:
        return self._device_arn

    @property
    def email(self) -> str:
        return self._email


class UserConverter:
    def parse_users(self, groups: list) -> List[User]:
        return [self._convert(row) for row in groups]

    @staticmethod
    def _convert(content: dict) -> User:
        return User(content["id"], content["device_arn"], content["email"])
