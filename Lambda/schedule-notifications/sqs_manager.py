import boto3
import json


class SqsManager:
    def __init__(self):
        self.sqs = boto3.client(
            service_name='sqs',
            region_name='eu-central-1'
        )

    def create_send_sms_event(self, message):
        self.sqs.send_message(
            QueueUrl='https://sqs.eu-central-1.amazonaws.com/007108578073/send-sms.fifo',
            MessageAttributes=message,
            MessageBody=json.dumps(message),
            MessageGroupId=(
                'CreateSendSmsEvent'
            )
        )

    def create_send_email_event(self, message):
        self.sqs.send_message(
            QueueUrl='https://sqs.eu-central-1.amazonaws.com/007108578073/send-email.fifo',
            MessageAttributes=message,
            MessageBody=json.dumps(message),
            MessageGroupId=(
                'CreateSendEmailEvent'
            )
        )