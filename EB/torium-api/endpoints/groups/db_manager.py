from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def delete_users_group(self, data):
        query = """
            DELETE FROM
                users_groups
            WHERE
                group_id = %(group_id)s
        """
        self.execute_query(query, data)

    def delete_group_invitation_logs(self, data):
        query = """
            DELETE FROM
                group_invitation_logs
            WHERE
                group_id = %(group_id)s
        """
        self.execute_query(query, data)

    def delete_events(self, data):
        query = """
            DELETE FROM
                events
            WHERE
                group_id = %(group_id)s
        """
        self.execute_query(query, data)

    def delete_group(self, data):
        query = """
            DELETE FROM
                groups
            WHERE
                id = %(id)s
        """
        self.execute_query(query, data)

    def valid_permission(self, data):
        query = """
            SELECT
                1
            FROM
                groups
            WHERE
                id = %(group_id)s
            AND
                admin_id = %(admin_id)s
        """
        return self.fetch_one(query, data)

    def post_group(self, data):
        query = """
            INSERT INTO
                groups
            (name, admin_id, timestamp)
            VALUES
            (%(name)s, %(admin_id)s, %(timestamp)s)
        """
        self.execute_query(query, data)

    def get_groups(self, data):
        query = """
            SELECT
                g.id,
                g.name,
                g.admin_id
            FROM
                groups g
            LEFT JOIN
                users_groups ug
            ON 
                ug.group_id = g.id
            WHERE
                ug.user_id = %(user_id)s
            OR 
                g.admin_id = %(user_id)s
        """
        return self.fetch_all(query, data)

    def update_group(self, data):
        query = """
            UPDATE
                groups
            SET
                name = %(name)s,
                admin_id = %(admin_id)s
            WHERE
                id = %(id)s
        """
        self.execute_query(query, data)