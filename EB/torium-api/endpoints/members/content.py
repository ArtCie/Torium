from typing import Optional
from datetime import datetime


class Content:
    def __init__(self, user_id: int, group_id: int, status: Optional[str]):
        self._group_id = group_id
        self._user_id = user_id
        self._status = status
        self._timestamp = datetime.now()

    @property
    def group_id(self) -> int:
        return self._group_id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def status(self) -> str:
        return self._status

    @property
    def timestamp(self) -> datetime:
        return self._timestamp


class ContentMember:
    def __init__(self, user_id: int, username: str, email: str, status: str):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._status = status

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def status(self) -> str:
        return self._status


class ContentConverter:
    @staticmethod
    def convert(content: dict, status=None) -> Content:
        return Content(content["user_id"], content["group_id"], status)

    @staticmethod
    def convert_members(content: dict) -> ContentMember:
        return ContentMember(content["id"], content["username"], content["email"], content["status"])