class Content:
    def __init__(self, email: str, cognito_user_id: str):
        self._email = email
        self._cognito_user_id = cognito_user_id

    @property
    def email(self) -> str:
        return self._email

    @property
    def cognito_user_id(self) -> str:
        return self._cognito_user_id


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content['request']['userAttributes']['email'], content['userName'])
