class User:
    def __init__(self, user_id: int, email: str, mobile_number: str, device_arn: str, reminder_preferences: str, url: str):
        self._user_id = user_id
        self._email = email
        self._mobile_number = mobile_number
        self._device_arn = device_arn
        self._reminder_preferences = reminder_preferences
        self._url = url

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def email(self) -> str:
        return self._email

    @property
    def mobile_number(self) -> str:
        return self._mobile_number

    @property
    def device_arn(self) -> str:
        return self._device_arn

    @property
    def reminder_preferences(self) -> str:
        return self._reminder_preferences

    @property
    def url(self) -> str:
        return self._url


class UserBuilder:
    @staticmethod
    def build_users(users) -> list:
        return [User(**user) for user in users]