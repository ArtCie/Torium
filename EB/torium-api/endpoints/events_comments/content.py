import datetime


class Content:
    def __init__(self, id: int, event_id: int, user_id: int, comment: str):
        self._id = id
        self._event_id = event_id
        self._user_id = user_id
        self._comment = comment
        self._timestamp = datetime.datetime.utcnow()

    @property
    def id(self) -> int:
        return self._id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def event_id(self) -> int:
        return self._event_id

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def timestamp(self) -> datetime:
        return self._timestamp


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content.get("id"), content.get("event_id"), content.get("user_id"),
                       content.get("comment"))
