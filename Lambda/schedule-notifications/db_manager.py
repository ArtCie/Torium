from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def get_event_users(self, data):
        query = """    
            SELECT
                u.email,
                u.mobile_number,
                u.device_arn,
                u.user_id,
                u.reminder_preferences,
                o.url
            FROM
                events_users eu
            INNER JOIN
                users u
            ON 
                u.id = events_users.user_id
            LEFT JOIN
                organizations o 
            ON 
                o.id = u.organization_id
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
            )
            RETURNING id;
        """
        return self.fetch_one(query, data)

    def get_event_details(self, data):
        query = """
            SELECT
                is_budget,
                budget,
                name
                description
            FROM
                events
            WHERE
                id = %(event_id)s
        """
        return self.fetch_one(query, data)