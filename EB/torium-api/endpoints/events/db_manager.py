from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def post_event(self, data):
        query = """
            INSERT INTO
                events
            (   
                is_budget,
                budget,
                description,
                group_id,
                event_timestamp,
                reminder,
                schedule_period,
                timestamp,
                name
            )
            VALUES
            (
                %(is_budget)s,
                %(budget)s,
                %(description)s,
                %(group_id)s,
                %(event_timestamp)s,
                %(reminder)s,
                %(schedule_period)s,
                %(timestamp)s,
                %(name)s
            )
            RETURNING id;
        """
        return self.fetch_one(query, data)

    def insert_event_user(self, data):
        query = """
            INSERT INTO
                events_users
            (
                event_id,
                user_id,
                timestamp
            )
            VALUES
            (
                %(event_id)s,
                %(user_id)s,
                %(timestamp)s
            )
        """
        self.execute_query(query, data)

    def update_event(self, data):
        query = """
            UPDATE
                events
            SET
                is_budget = %(is_budget)s,
                budget = %(budget)s,
                description = %(description)s,
                group_id = %(group_id)s,
                event_timestamp = %(event_timestamp)s,
                reminder = %(reminder)s,
                schedule_period = %(schedule_period)s,
                updated_timestamp = %(timestamp)s,
                name = %(name)s
            WHERE 
                id = %(id)s;
        """
        self.execute_query(query, data)

    def select_event_users(self, data):
        query = """
            SELECT
                user_id
            FROM
                events_users
            WHERE
                event_id = %(id)s
        """
        return self.fetch_all(query, data)

    def delete_event_user(self, data):
        query = """
            DELETE FROM
                events_users
            WHERE
                user_id = %(user_id)s
            AND 
                event_id = %(event_id)s
        """
        self.execute_query(query, data)

    def valid_user_event_relation(self, data):
        query = """
            SELECT 
                1
            FROM 
                users_groups ug
            INNER JOIN 
                events_users eu 
            ON 
                ug.user_id = eu.user_id 
            WHERE 
                ug.status = 'admin'
            AND 
                eu.user_id = %(user_id)s
            AND 
                eu.event_id = %(event_id)s
        """
        return self.fetch_one(query, data)

    def delete_event_users(self, data):
        query = """
            DELETE FROM
                events_users
            WHERE
                event_id = %(event_id)s
        """
        self.execute_query(query, data)

    def delete_event(self, data):
        query = """
            DELETE FROM
                events
            WHERE
                id = %(event_id)s
        """
        self.execute_query(query, data)

    def get_user_events(self, data):
        query = """
            SELECT
                e.id,
                e.budget,
                e.is_budget,
                e.description,
                e.group_id,
                e.event_timestamp,
                e.reminder,
                e.schedule_period,
                e.name,
                g.name as group_name,
                ARRAY(SELECT user_id from events_users WHERE event_id = e.id) as users
            FROM
                events e 
            INNER JOIN
                events_users eu
            ON 
                e.id = eu.event_id
            INNER JOIN
                groups g 
            ON
                g.id = e.group_id
            WHERE
                eu.user_id = %(user_id)s
            ORDER BY
                e.event_timestamp
            ASC
        """
        return self.fetch_all(query, data)

    def get_user_group_events(self, data):
        query = """
            SELECT
                e.id,
                e.budget,
                e.is_budget,
                e.description,
                e.group_id,
                e.event_timestamp,
                e.reminder,
                e.schedule_period,
                e.name,
                g.name as group_name,
                ARRAY(SELECT user_id from events_users WHERE event_id = e.id) as users
            FROM
                events e 
            INNER JOIN
                events_users eu
            ON 
                e.id = eu.event_id
            INNER JOIN
                groups g 
            ON
                g.id = e.group_id
            WHERE
                eu.user_id = %(user_id)s
            AND
                e.group_id = %(group_id)s
            ORDER BY
                e.event_timestamp
            ASC
        """
        return self.fetch_all(query, data)

    def valid_latency(self, data):
        query = """
            SELECT
                1
            FROM
                event_reminders
            WHERE
                now() - trigger_timestamp > '1 day'::interval
            AND 
                event_id = %(event_id)s
        """
        return self.fetch_one(query, data)

    def select_event_timestamp(self, data):
        query = """
            SELECT
                event_timestamp
            FROM
                events
            WHERE
                id = %(event_id)s
        """
        return self.fetch_one(query, data)