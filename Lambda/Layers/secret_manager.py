import boto3
from json import loads


class SecretManager:
    def __init__(self):
        self.client = boto3.client('secretsmanager')
        self.TODDY_SECRET_ID = 'toddy-secret'
        self.PINPOINT_APP_ID = 'pinpoint_app_id'

    def get_db_config(self):
        response = self.client.get_secret_value(
            SecretId=self.TODDY_SECRET_ID
        )['SecretString']
        return DatabaseConfig(**loads(response))

    def get_pinpoint_app_id(self):
        response = self.client.get_secret_value(
            SecretId=self.PINPOINT_APP_ID
        )['SecretString']
        return loads(response)["app_id"]


class DatabaseConfig:
    def __init__(self, host: str, user: str, database: str, password: str):
        self._host = host
        self._user = user
        self._database = database
        self._password = password

    @property
    def host(self) -> str:
        return self._host

    @property
    def user(self) -> str:
        return self._user

    @property
    def database(self) -> str:
        return self._database

    @property
    def password(self) -> str:
        return self._password
