from logger import log
from utils import log_exception, build_response

from db_manager import DBManager
from resources.content import Content


class PostSignUpManager:
    @log
    def __init__(self, db_manager: DBManager, content: Content):
        self._db_manager = db_manager
        self._content = content

    @log
    def process(self) -> None:
        try:
            self._update_user()
            self._db_manager.commit_changes()
        except Exception as e:
            log_exception(type(self).__name__, str(e))
            self._db_manager.rollback_changes()
        finally:
            self._db_manager.close_cursor()
            self._db_manager.close_connection()

    def _update_user(self):
        data = self._build_data()
        self._db_manager.update_user(data)

    def _build_data(self):
        return {
            "is_confirmed": True,
            "cognito_user_id": self._content.cognito_user_id
        }

