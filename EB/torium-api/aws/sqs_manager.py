import boto3 as boto3
import json


class SqsManager:
    def __init__(self):
        self.sqs = boto3.client(
            service_name='sqs',
            region_name='eu-central-1'
        )

    def create_sqs_notify_event_message(self, message: dict):
        self.sqs.send_message(
            QueueUrl="insert_queue_url_here",
            MessageAttributes=message,
            MessageBody=json.dumps(message),
            MessageGroupId=(
                'CreateNotifyEventEvent'
            )
        )
