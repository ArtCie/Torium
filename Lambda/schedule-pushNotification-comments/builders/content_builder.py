from datetime import datetime


class Content:
    def __init__(self, content: dict):
        self._user_id = content["user_id"]["StringValue"]
        self._sent_timestamp = content["event_timestamp"]["StringValue"]
        self._events_comments_id = content["events_comments_id"]["StringValue"]
        self._event_id = content["event_id"]["StringValue"]
        self._comment = content["comment"]["StringValue"]
        self._timestamp = datetime.utcnow()

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def sent_timestamp(self) -> str:
        return self._sent_timestamp

    @property
    def events_comments_id(self) -> str:
        return self._events_comments_id

    @property
    def event_id(self) -> str:
        return self._event_id

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def timestamp(self) -> datetime:
        return self._timestamp
