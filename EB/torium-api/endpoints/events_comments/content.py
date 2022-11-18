import datetime


class Content:
    def __init__(self, id: int, event_id: int, user_id: int, comment: str, event_timestamp: datetime):
        self._id = id
        self._event_id = event_id
        self._user_id = user_id
        self._comment = comment
        self._timestamp = datetime.datetime.now()
        self._event_timestamp = self._get_relative_timestamp(event_timestamp) if event_timestamp else None

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

    @property
    def event_timestamp(self) -> str:
        return self._event_timestamp

    def _get_relative_timestamp(self, event_timestamp: datetime) -> str:
        INTERVALS = (
            ('y', 217728000),
            ('mon', 18144000),
            ('w', 604800),
            ('d', 86400),
            ('h', 3600),
            ('min', 60),
            ('s', 1),
        )
        seconds = self._timestamp.timestamp() - event_timestamp.timestamp()
        for name, count in INTERVALS:
            value = seconds // count
            if value:
                return f"{int(value)}{name} ago"


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content.get("id"), content.get("event_id"), content.get("user_id"),
                       content.get("comment"), content.get("event_timestamp"))
