from logger import log
from utils import log_exception, build_response

from db_manager import DBManager

from datetime import datetime
from sqs_manager import SqsManager
from user_builder import UserBuilder, User
import json


class ScheduleNotificationsManager:
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
            return self._build_response(str(e), 200)
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
            'trigger_timestamp': self._event_timestamp,
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
                self._send_push_sqs(user, event_reminders_id, event)

    @staticmethod
    def _build_message(event: dict, user: User):
        message = f"""Torium reminder!
Event name: 
{event["name"]}

Description: 
{event["description"]}

Timestamp: 
{event["event_timestamp"].strftime("%d %b %Y, %H:%M:%S")}

"""
        if event["is_budget"]:
            message += f"""Budget for this event was set to {event['budget']} PLN
"""
            if user.url:
                message += f"""Your share = {round(float(event['budget']) / event['users_count'], 2)} PLN, you can pay it here: {user.url}"""
        return message

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

    def _send_push_sqs(self, user: User, event_reminders_id: int, event: dict):
        message = {
            "device_arn": {
                "DataType": "String",
                "StringValue": user.device_arn
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
            "title": {
                "DataType": "String",
                "StringValue": "Torium reminder!"
            },
            "body": {
                "DataType": "String",
                "StringValue": self._get_notification_body(event)
            },
            "forward_link": {
                "DataType": "String",
                "StringValue": user.url if user.url else "None"
            }
        }
        self._sqs_manager.create_send_push_notification_event(message)

    @staticmethod
    def _get_notification_body(event: dict):
        result = f"""{event["name"]}
{event["description"]}
        """
        if event["is_budget"]:
            result += f"Budget for this event was set to {event['budget']} Pay your share now!"
        return result
