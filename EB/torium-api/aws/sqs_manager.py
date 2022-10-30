import boto3 as boto3
import json


class SqsManager:
    def __init__(self):
        self.sqs = boto3.client(
            service_name='sqs',
            region_name='eu-central-1'
        )

    def create_sqs_schedule_notifications_event(self, message: dict) -> None:
        self.sqs.send_message(
            QueueUrl='https://sqs.eu-central-1.amazonaws.com/007108578073/schedule-notifications-queue.fifo',
            MessageAttributes=message,
            MessageBody=json.dumps(message),
            MessageGroupId=(
                'CreateScheduleNotificationsEvent'
            )
        )

    def create_sqs_schedule_push_notification_comments_event(self, message):
        self.sqs.send_message(
            QueueUrl='https://sqs.eu-central-1.amazonaws.com/007108578073/schedule-push-notification-comments-queue'
                     '.fifo',
            MessageAttributes=message,
            MessageBody=json.dumps(message),
            MessageGroupId=(
                'CreateSchedulePushNotificationCommentsEvent'
            )
        )