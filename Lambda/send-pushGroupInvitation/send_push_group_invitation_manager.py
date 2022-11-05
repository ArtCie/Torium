from logger import log
from utils import log_exception, build_response

from db_manager import DBManager

from sns_manager import SnsManager
from content_builder import Content
import json


class SendPushGroupInvitationManager:
    @log
    def __init__(self, db_manager: DBManager, content):
        self._db_manager = db_manager
        self._sns_manager = SnsManager()
        self._content = Content(content)
        self.STATUS = "sent"

    @log
    def process(self) -> dict:
        try:
            self._handle_event()
            self._db_manager.commit_changes()
            return self._build_response('OK', 200)
        except Exception as e:
            log_exception(type(self).__name__, str(e))
            self._db_manager.rollback_changes()
            return self._build_response(str(e), 200)
        finally:
            self._db_manager.close_cursor()
            self._db_manager.close_connection()

    def _handle_event(self):
        device_arn = self._select_user_device_arn()
        group_data = self._select_group_data()
        self._sns_manager.publish(device_arn, group_data)
        self._update_group_invitation_logs()

    def _select_user_device_arn(self):
        data = {
            "user_id": self._content.user_id
        }
        return self._db_manager.select_user_device_arn(data)[0]

    def _select_group_data(self):
        data = {
            "group_id": self._content.group_id
        }
        return self._db_manager.select_group_data(data)

    @staticmethod
    def _build_response(message: str, response_code: int) -> dict:
        return {
            'statusCode': response_code,
            'body': json.dumps(message)
        }

    def _update_group_invitation_logs(self):
        data = {
            "group_invitation_logs_id": self._content.group_invitation_logs_id,
            "status": self.STATUS,
            "updated_timestamp": self._content.timestamp
        }
        self._db_manager.update_group_invitation_logs(data)

