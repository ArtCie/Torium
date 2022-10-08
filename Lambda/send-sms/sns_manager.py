import boto3


class SnsManager:
    def __init__(self):
        self.sns = boto3.client(
            service_name='sns',
            region_name='eu-central-1'
        )

    def create_send_sms_event(self, phone_number: str, message: str) -> None:
        self.sns.publish(
            PhoneNumber=phone_number,
            Message=message
        )

