from logger import log
from typing import List

from utils import log_exception

from db_manager import DBManager

from sns_manager import SnsManager
from builders.content_builder import Content
from builders.user_builder import UserConverter, User
import json


class SchedulePushNotificationCommentsManager:
    @log
    def __init__(self, db_manager: DBManager, content):
        self._db_manager = db_manager
        self._sns_manager = SnsManager()
        self._content = Content(content)
        self._user_converter = UserConverter()

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
        users_to_send_notification = self._get_users_comment_notification()
        event_name = self._get_event_name()
        self._send_comment_notifications(users_to_send_notification, event_name)

    def _get_users_comment_notification(self):
        data = {
            "event_id": self._content.event_id,
            "user_id": self._content.user_id
        }
        result = self._db_manager.get_users_comment_notification(data)
        return self._user_converter.parse_users(result)

    def _get_event_name(self):
        data = {
            "event_id": self._content.event_id
        }
        return self._db_manager.get_event_name(data)[0]

    def _send_comment_notifications(self, users: List[User], event_name: str):
        for user in users:
            try:
                self._insert_event_comments_logs(user.user_id)
                title, body = self._get_sns_attributes(user, event_name)
                self._sns_manager.publish(title, body, user.device_arn, self._content.event_id)
            except Exception as e:
                log_exception(type(self).__name__, str(e))

    def _insert_event_comments_logs(self, user_id: int):
        data = {
            "events_comments_id": self._content.events_comments_id,
            "sent_timestamp": self._content.sent_timestamp,
            "user_id": user_id,
            "timestamp": self._content.timestamp
        }
        self._db_manager.insert_event_comments_logs(data)

    def _get_sns_attributes(self, user: User, event_name: str):
        title = f"New comment: {event_name}"
        body = f"{user.email}: {self._content.comment[:7]}"
        if len(self._content.comment) > 7:
            body += "..."
        return title, body

    @staticmethod
    def _build_response(message: str, response_code: int) -> dict:
        return {
            'statusCode': response_code,
            'body': json.dumps(message)
        }
