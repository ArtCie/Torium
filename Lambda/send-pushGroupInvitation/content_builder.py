from datetime import datetime


class Content:
    def __init__(self, content: dict):
        self._user_id = content["user_id"]["StringValue"]
        self._group_invitation_logs_id = content["group_invitation_logs_id"]["StringValue"]
        self._group_id = content["group_id"]["StringValue"]
        self._timestamp = datetime.utcnow()

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def group_invitation_logs_id(self) -> str:
        return self._group_invitation_logs_id

    @property
    def group_id(self) -> str:
        return self._group_id

    @property
    def timestamp(self) -> datetime:
        return self._timestamp
