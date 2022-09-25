import boto3
from json import loads


class SecretManager:
    def __init__(self):
        self.client = boto3.client('secretsmanager', region='eu-central-1')
        self.SECRET_ID = 'toddy-secret'

    def get_db_config(self):
        response = self.client.get_secret_value(
            SecretId=self.SECRET_ID
        )['SecretString']
        return DatabaseConfig(**loads(response))


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
