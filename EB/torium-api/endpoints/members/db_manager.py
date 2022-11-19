from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def post_member(self, data):
        query = """
            INSERT INTO
                group_invitation_logs
                (group_id, user_to, timestamp, status)
            VALUES
                (%(group_id)s, %(user_id)s, %(timestamp)s, %(status)s)
            RETURNING id
        """
        return self.fetch_one(query, data)

    def delete_invitation(self, data):
        query = """
            DELETE FROM
                group_invitation_logs
            WHERE
                user_to = %(user_id)s
            AND 
                group_id = %(group_id)s
        """
        self.execute_query(query, data)

    def delete_member(self, data):
        query = """
            DELETE FROM
                users_groups
            WHERE
                user_id = %(user_id)s
            AND 
                group_id = %(group_id)s
        """
        self.execute_query(query, data)

    def get_members(self, data):
        query = """
            SELECT
                u.id,
                u.username,
                u.email,
                ug.status
            FROM
                users_groups ug
            INNER JOIN
                users u 
            ON 
                u.id = ug.user_id
            WHERE
                ug.user_id != %(user_id)s
            AND 
                ug.group_id = %(group_id)s
        """
        return self.fetch_all(query, data)

    def update_group_invitation_logs(self, data):
        query = """
            UPDATE
                group_invitation_logs
            SET
                status = %(status)s,
                updated_timestamp = %(updated_timestamp)s
            WHERE 
                group_id = %(group_id)s
            AND 
                user_to = %(user_id)s        
        """
        self.execute_query(query, data)

    def insert_users_groups(self, data):
        query = """
            INSERT INTO
                users_groups
                (group_id, user_id, status, timestamp)
            VALUES
                (%(group_id)s, %(user_id)s, %(status)s, %(timestamp)s)
        """
        self.execute_query(query, data)

    def valid_permissions(self, data):
        query = """
            SELECT 
                1
            FROM
                users_groups
            WHERE
                group_id = %(group_id)s
            AND 
                user_id = %(admin_id)s
            AND 
                status = %(status)s
        """
        return self.fetch_one(query, data)

    def valid_moderator_permissions(self, data):
        query = """
            SELECT 
                1
            FROM
                users_groups
            WHERE
                group_id = %(group_id)s
            AND 
                user_id = %(admin_id)s
            AND
                ( 
                    status = %(status_moderator)s
                OR
                    status = %(status_admin)s
                )
        """
        return self.fetch_one(query, data)

    def update_users_group_status(self, data):
        query = """
            UPDATE
                users_groups
            SET
                status = %(status)s
            WHERE
                group_id = %(group_id)s
            AND 
                user_id = %(user_id)s
        """
        self.execute_query(query, data)

    def is_invitation_sent(self, data):
        query = """
            SELECT
                1
            FROM
                group_invitation_logs
            WHERE
                user_to = %(user_id)s
            AND
                group_id = %(group_id)s
            AND
                (
                    status = %(status_sent)s
                OR
                    status = %(status_pending)s
                )
        """
        return self.fetch_one(query, data)

    def delete_events(self, data):
        query = """
            DELETE FROM
                events_users
            WHERE
                user_id = %(user_id)s
            AND
                event_id in (
                    SELECT
                        e.id
                    FROM
                        events e
                    WHERE
                        group_id = %(group_id)s
                )
        """

    def delete_comments(self, data):
        query = """
            DELETE FROM
                events_comments
            WHERE
                user_id = %(user_id)s
            AND 
                event_id in (
                    SELECT
                        e.id
                    FROM
                        events e
                    WHERE
                        group_id = %(group_id)s
                )
        """
        self.execute_query(query, data)