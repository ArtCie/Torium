from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def insert_event_comments_logs(self, data):
        query = """
            INSERT INTO
            events_comments_logs
            (
                events_comments_id,
                sent_timestamp,
                user_id,
                timestamp
            )
            VALUES
            (
                %(events_comments_id)s,
                %(sent_timestamp)s,
                %(user_id)s,
                %(timestamp)s
            )
        """
        self.execute_query(query, data)

    def get_users_comment_notification(self, data):
        query = """
            SELECT
                u.id,
                u.device_arn,
                u.email
            FROM
                users u
            INNER JOIN
                events_users eu
            ON 
                eu.user_id = u.id
            WHERE
                eu.event_id = %(event_id)s
            AND 
                eu.user_id != %(user_id)s
            AND 
                u.device_arn IS NOT NULL
        """
        return self.fetch_all(query, data)

    def get_event_name(self, data):
        query = """
            SELECT
                name
            FROM
                events
            WHERE
                id = %(event_id)s
        """
        return self.fetch_one(query, data)