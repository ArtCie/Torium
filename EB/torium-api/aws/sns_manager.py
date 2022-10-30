import boto3
import os


class SnsManager:
    def __init__(self):
        self.sns = boto3.client(
            'sns',
            region_name='eu-central-1'
        )

    def send_message(self, phone_number: str, message: str) -> None:
        self.sns.publish(PhoneNumber=phone_number, Message=message)

    def add_endpoint(self, user_id: str, device_token: str) -> str:
        response = self.sns.create_platform_endpoint(
            PlatformApplicationArn=os.environ['PLATFORM_APPLICATION_ARN'],
            Token=device_token,
            CustomUserData=self._create_description(user_id, device_token)
        )
        return response['EndpointArn']

    @staticmethod
    def _create_description(user_id: str, device_token: str) -> str:
        return f"{user_id=}, {device_token=}"

    def update_token_in_sns_endpoint(self, user_id: str, endpoint_arn: str, device_token: str) -> None:
        self.sns.set_endpoint_attributes(
            EndpointArn=endpoint_arn,
            Attributes={
                'Token': device_token,
                'CustomUserData': self._create_description(user_id, device_token)
            }
        )