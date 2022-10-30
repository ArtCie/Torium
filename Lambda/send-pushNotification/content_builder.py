from datetime import datetime


class Content:
    def __init__(self, content: dict):
        self._user_id = content["user_id"]["StringValue"]
        self._sent_timestamp = content["event_timestamp"]["StringValue"]
        self._event_reminders_id = content["event_reminders_id"]["StringValue"]
        self._device_arn = content["device_arn"]["StringValue"]
        self._title = content["title"]["StringValue"]
        self._body = content["body"]["StringValue"]
        self._forward_link = content["forward_link"]["StringValue"]
        self._timestamp = datetime.utcnow()

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
    def device_arn(self) -> str:
        return self._device_arn

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def title(self) -> str:
        return self._title

    @property
    def body(self) -> str:
        return self._body

    @property
    def forward_link(self) -> str:
        return self._forward_link


