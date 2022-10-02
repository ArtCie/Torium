from datetime import datetime
from typing import Optional


class Content:
    def __init__(self, id: int, is_budget: bool, budget: float,
                 description: str, group_id: int, event_timestamp: datetime,
                 reminder: str, schedule_period: str, users: Optional[list]):
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
    def event_timestamp(self) -> datetime:
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


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content.get("id"), content["is_budget"], content["budget"],
                       content["description"], content["event_timestamp"], content["group_id"],
                       content["reminder"], content["schedule_period"], content["users"])
