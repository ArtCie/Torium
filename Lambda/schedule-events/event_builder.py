from datetime import datetime


class Event:
    def __init__(self, id: int, timestamp: datetime):
        self._id = id
        self._timestamp = timestamp

    @property
    def id(self) -> int:
        return self._id

    @property
    def timestamp(self) -> datetime:
        return self._timestamp


class EventBuilder:
    @staticmethod
    def build_events(events) -> list:
        return [Event(event["id"], event["event_timestamp"]) for event in events]