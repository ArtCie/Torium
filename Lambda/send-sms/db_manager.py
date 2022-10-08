from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def insert_event_reminders_logs(self, data):
        query = """
            INSERT INTO
            (
                event_reminders_id,
                sent_timestamp,
                user_id,
                timestamp
            )
            VALUES
            (
                %(event_reminders_id)s,
                %(sent_timestamp)s,
                %(user_id)s,
                %(timestamp)s
            )
        """
        self.execute_query(query, data)
