class Content:
    def __init__(self, group_id: int, email: str, name: str):
        self._group_id = group_id
        self._email = email
        self._name = name

    @property
    def group_id(self) -> int:
        return self._group_id

    @property
    def email(self) -> str:
        return self._email

    @property
    def name(self) -> str:
        return self._name


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content["group_id"], content["email"], content["name"])

