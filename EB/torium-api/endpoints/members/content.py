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


class ContentConverter:
    @staticmethod
    def convert(content: dict, status=None) -> Content:
        return Content(content["user_id"], content["group_id"], status)
