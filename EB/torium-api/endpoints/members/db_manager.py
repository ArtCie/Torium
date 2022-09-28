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
                u.email
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
                user_id = %(user_id)        
        """
        self.execute_query(query, data)

    def insert_users_groups(self, data):
        query = """
            INSERT INTO
                users_groups
                (group_id, user_id, timemstamp)
            VALUES
                (%(group_id)s, %(user_id)s, %(timestamp)s)
        """
        self.execute_query(query, data)