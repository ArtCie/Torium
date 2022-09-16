class Content:
    def __init__(self, cognito_user_id: str):
        self._cognito_user_id = cognito_user_id

    @property
    def cognito_user_id(self) -> str:
        return self._cognito_user_id


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content['userName'])
