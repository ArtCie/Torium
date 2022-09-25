from database.secret_manager import DatabaseConfig
import psycopg2
from psycopg2 import extras


class DBManagerBase:
    def __init__(self, database_config: DatabaseConfig):
        self.connection = None
        self.cursor = None
        self.database_config = database_config

    def connect(self):
        self.connection = psycopg2.connect(
            user=self.database_config.user,
            host=self.database_config.host,
            password=self.database_config.password,
            database=self.database_config.database
        )
        self.connection.autocommit = False
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def rollback_changes(self):
        if self.connection:
            self.connection.rollback()

    def commit_changes(self):
        self.connection.commit()

    def close_database(self):
        self.close_cursor()
        self.close_connection()

    def close_cursor(self):
        if self.cursor:
            self.cursor.close()

    def close_connection(self):
        if self.connection and not self.connection.closed:
            self.connection.close()

    def fetch_one(self, query, data):
        self.execute_query(query, data)
        return self.cursor.fetchone()

    def fetch_all(self, query, data):
        self.execute_query(query, data)
        return self.cursor.fetchall()

    def execute_query(self, query, data):
        self.cursor.execute(query, data)
