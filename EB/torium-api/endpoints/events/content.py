from datetime import datetime
from typing import Optional


class Content:
    def __init__(self, id: int, is_budget: bool, budget: float,
                 description: str, group_id: int, event_timestamp: str,
                 reminder: str, schedule_period: str, users: Optional[list],
                 name: str, group_name: str):
        self._id = id
        self._is_budget = is_budget
        self._budget = budget
        self._description = description
        self._group_id = group_id
        self._event_timestamp = event_timestamp
        self._reminder = reminder
        self._schedule_period = schedule_period
        self._timestamp = datetime.utcnow()
        self._users = users
        self._name = name
        self._group_name = group_name

    @property
    def id(self) -> int:
        return self._id

    @property
    def is_budget(self) -> bool:
        return self._is_budget

    @property
    def budget(self) -> float:
        return self._budget

    @property
    def description(self) -> str:
        return self._description

    @property
    def event_timestamp(self) -> str:
        return self._event_timestamp

    @property
    def group_id(self) -> int:
        return self._group_id

    @property
    def reminder(self) -> str:
        return self._reminder

    @property
    def schedule_period(self) -> str:
        return self._schedule_period

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def users(self) -> list:
        return self._users

    @property
    def name(self) -> str:
        return self._name

    @property
    def group_name(self) -> str:
        return self._group_name


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content.get("id"), content["is_budget"], content["budget"],
                       content["description"], content["group_id"], str(content["event_timestamp"]),
                       content["reminder"], str(content["schedule_period"]), content.get("users", []),
                       content["name"], content.get("group_name"))
