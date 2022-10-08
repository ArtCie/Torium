from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def get_event_users(self, data):
        query = """    
            SELECT
                u.email,
                u.mobile_number,
                u.device_arn,
                u.user_id,
                u.reminder_preferences
            FROM
                events_users eu
            INNER JOIN
                users u
            ON 
                u.id = events_users.user_id
            WHERE
                eu.event_id = %(event_id)s
        """
        return self.fetch_all(query, data)

    def insert_event_reminders(self, data):
        query = """
            INSERT INTO
                event_reminders
            (
                event_id,
                event_timestamp,
                timestamp
            )
            VALUES
            (
                %(event_id)s,
                %(event_timestamp)s,
                %(timestamp)s
            RETURNING id;
        """
        return self.fetch_one(query, data)
