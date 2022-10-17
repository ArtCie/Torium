from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def update_user(self, data):
        query = """
            UPDATE
                users
            SET
                is_confirmed = %(is_confirmed)s
            WHERE
                cognito_user_id = %(cognito_user_id)s
            RETURNING
                id
        """
        self.fetch_one(query, data)
