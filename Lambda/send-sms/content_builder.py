from datetime import datetime


class Content:
    def __init__(self, content: dict):
        self._user_id = content["user_id"]["StringValue"]
        self._sent_timestamp = content["event_timestamp"]["StringValue"]
        self._event_reminders_id = content["event_reminders_id"]["StringValue"]
        self._mobile_number = content["mobile_number"]["StringValue"]
        self._message = content["message"]["StringValue"]
        self._timestamp = datetime.now()

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def sent_timestamp(self) -> str:
        return self._sent_timestamp

    @property
    def event_reminders_id(self) -> str:
        return self._event_reminders_id

    @property
    def mobile_number(self) -> str:
        return self._mobile_number

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def message(self) -> str:
        return self._message
