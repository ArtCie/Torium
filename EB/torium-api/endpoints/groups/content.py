from datetime import datetime
from typing import Optional


class Content:
    def __init__(self, group_id: Optional[int], name: Optional[str], admin_id: int):
        self._group_id = group_id
        self._name = name
        self._admin_id = admin_id
        self._timestamp = datetime.now()

    @property
    def group_id(self) -> int:
        return self._group_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def admin_id(self) -> int:
        return self._admin_id

    @property
    def timestamp(self) -> datetime:
        return self._timestamp


class ContentConverter:
    @staticmethod
    def convert_post(content: dict) -> Content:
        return Content(None, content["name"], content["admin_id"])

    @staticmethod
    def convert_delete(content: dict) -> Content:
        return Content(content["id"], None, content["admin_id"])

    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content["id"], content["name"], content["admin_id"])
