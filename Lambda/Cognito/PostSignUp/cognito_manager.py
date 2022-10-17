import boto3
import os


class CognitoManager:
    def __init__(self):
        self.client = boto3.client(service_name='cognito-idp')

    def update_cognito_user_pool(self, cognito_user_id: str, user_id: int):
        response = self.client.admin_update_user_attributes(
            UserPoolId=os.environ['COGNITO_USER_POOL_ID'],
            Username=cognito_user_id,
            UserAttributes=[
                {
                    'Name': 'custom:user_id',
                    'Value': str(user_id)
                },
            ],
            ClientMetadata={
                'string': 'string'
            }
        )
