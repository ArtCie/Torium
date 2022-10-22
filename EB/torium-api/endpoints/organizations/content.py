class Content:
    def __init__(self, id_: str, name: str, url: str, file_name: str):
        self._id = id_
        self._name = name
        self._url = url
        self._file_name = file_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def url(self) -> str:
        return self._url

    @property
    def file_name(self) -> str:
        return self._file_name

    @property
    def id(self) -> str:
        return self._id


class ContentConverter:
    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content["id"], content["name"], content["url"], content["file_name"])
