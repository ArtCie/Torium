from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def insert_user(self, data):
        query = """
            INSERT INTO
            users 
                (   
                email,
                timestamp,
                is_confirmed,
                cognito_user_id
                )
            VALUES
                (
                %(email)s,
                %(timestamp)s,
                %(is_confirmed)s,
                %(cognito_user_id)s
                )
        """
        self.execute_query(query, data)

