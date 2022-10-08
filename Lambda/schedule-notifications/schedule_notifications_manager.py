from logger import log
from utils import log_exception, build_response

from db_manager import DBManager

from datetime import datetime
from sqs_manager import SqsManager
from user_builder import UserBuilder, User
import json


class ScheduleEventsManager:
    @log
    def __init__(self, db_manager: DBManager, content):
        self._db_manager = db_manager
        self._sqs_manager = SqsManager()
        self._event_id = content["event_id"]["StringValue"]
        self._event_timestamp = content["event_timestamp"]["StringValue"]

    @log
    def process(self) -> dict:
        try:
            self._handle_event()
            self._db_manager.commit_changes()
            return self._build_response('OK', 200)
        except Exception as e:
            log_exception(type(self).__name__, str(e))
            self._db_manager.rollback_changes()
            return self._build_response(str(e), 500)
        finally:
            self._db_manager.close_cursor()
            self._db_manager.close_connection()

    def _handle_event(self):
        event_reminders_id = self._insert_event_reminders()
        users_to_send = self._get_event_users()
        self._send_reminders(users_to_send, event_reminders_id)

    def _get_event_users(self) -> list:
        data = {
            "event_id": self._event_id
        }
        result = self._db_manager.get_event_users(data)
        return UserBuilder.build_users(result)

    @staticmethod
    def _build_response(message: str, response_code: int) -> dict:
        return {
            'statusCode': response_code,
            'body': json.dumps(message)
        }

    def _insert_event_reminders(self) -> int:
        data = {
            'event_timestamp': self._event_timestamp,
            'event_id': self._event_id,
            'timestamp': datetime.utcnow()
        }
        return self._db_manager.insert_event_reminders(data)[0]

    def _send_reminders(self, users_to_send: list, event_reminders_id: int):
        event = self._get_event_details()
        for user in users_to_send:
            message = self._build_message(event, user)
            if user.reminder_preferences == "SMS":
                self._send_sms_sqs(user, event_reminders_id, message)
            elif user.reminder_preferences == "EMAIL":
                self._send_email_sqs(user, event_reminders_id, message)
            else:
                pass  # TODO PUSH

    @log
    def _send_sms_sqs(self, user: User, event_reminders_id: int, message: str):
        message = {
            "mobile_number": {
                "DataType": "String",
                "StringValue": str(user.mobile_number)
            },
            "user_id": {
                "DataType": "String",
                "StringValue": str(user.user_id)
            },
            "event_reminders_id": {
                "DataType": "String",
                "StringValue": str(event_reminders_id)
            },
            "event_timestamp": {
                "DataType": "String",
                "StringValue": str(self._event_timestamp)
            },
            "message": {
                "DataType": "String",
                "StringValue": str(message)
            }
        }
        self._sqs_manager.create_send_sms_event(message)

    @log
    def _send_email_sqs(self, user: User, event_reminders_id: int, message: str):
        message = {
            "email": {
                "DataType": "String",
                "StringValue": str(user.email)
            },
            "user_id": {
                "DataType": "String",
                "StringValue": str(user.user_id)
            },
            "event_reminders_id": {
                "DataType": "String",
                "StringValue": str(event_reminders_id)
            },
            "event_timestamp": {
                "DataType": "String",
                "StringValue": str(self._event_timestamp)
            },
            "message": {
                "DataType": "String",
                "StringValue": str(message)
            }
        }
        self._sqs_manager.create_send_email_event(message)

    def _get_event_details(self):
        data = {
            "event_id": self._event_id
        }
        return self._db_manager.get_event_details(data)

    @build_response
    def _build_message(event: dict, user: User):
        message = f"""
Torium reminder!
{event["name"]}:
Description: {event["description"]}

        """
        if user.url and event["is_budget"]:
            message += f"""Budget for this event was set to {event['budget']}
You can pay it here: {user.url}"""
        return message
