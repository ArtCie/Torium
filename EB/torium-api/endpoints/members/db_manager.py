from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def post_member(self, data):
        query = """
            INSERT INTO
                group_invitation_logs
                (group_id, user_to, timestamp, status)
            VALUES
                (%(group_id)s, %(user_id)s, %(timestamp)s, %(status)s)
        """
        self.execute_query(query, data)
