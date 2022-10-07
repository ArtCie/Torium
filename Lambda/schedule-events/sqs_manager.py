import boto3
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