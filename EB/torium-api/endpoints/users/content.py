from datetime import datetime
from typing import Optional


class Content:
    def __init__(self, user_id: int, username: Optional[str], email: Optional[str],
                 mobile_number: Optional[str], reminder_preferences: Optional[str],
                 cognito_user_id: Optional[str], device_arn: Optional[str], device_token: Optional[str],
                 organization_id: Optional[str], organization_name: Optional[str]):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._mobile_number = mobile_number
        self._reminder_preferences = reminder_preferences
        self._cognito_user_id = cognito_user_id
        self._device_arn = device_arn
        self._device_token = device_token
        self._organization_id = organization_id
        self._organization_name = organization_name
        self._timestamp = datetime.utcnow()

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def mobile_number(self) -> str:
        return self._mobile_number

    @property
    def reminder_preferences(self) -> str:
        return self._reminder_preferences

    @property
    def cognito_user_id(self) -> str:
        return self._cognito_user_id

    @property
    def device_arn(self) -> str:
        return self._device_arn

    @property
    def device_token(self) -> str:
        return self._device_token

    @property
    def organization_id(self) -> str:
        return self._organization_id

    @property
    def organization_name(self) -> str:
        return self._organization_name

    @property
    def timestamp(self) -> datetime:
        return self._timestamp


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content["user_id"], content.get("username"), content.get("email"), content.get("mobile_number"),
                       content.get("reminder_preferences"), content.get("cognito_user_id"), content.get("device_arn"),
                       content.get("device_token"), content.get("organization_id"), content.get("organization_name"))
