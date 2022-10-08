
class Event:
    def __init__(self, id: int,):
        self._id = id

    @property
    def id(self) -> int:
        return self._id


class EventBuilder:
    @staticmethod
    def build_events(events) -> list:
        return [Event(event["id"]) for event in events]