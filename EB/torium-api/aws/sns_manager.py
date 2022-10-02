import boto3


class SnsManager:
    def __init__(self):
        self.sns = boto3.client(
            'sns',
            region_name='eu-central-1'
        )

    def send_message(self, phone_number: str, message: str):
        self.sns.publish(PhoneNumber=phone_number, Message=message)
