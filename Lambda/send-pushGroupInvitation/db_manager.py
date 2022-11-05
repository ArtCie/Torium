from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def select_user_device_arn(self, data):
        query = """
            SELECT
                device_arn
            FROM
                users
            WHERE
                id = %(user_id)s
        """
        return self.fetch_one(query, data)

    def select_group_data(self, data):
        query = """
            SELECT
                g.name,
                u.email
            FROM
                groups g 
            INNER JOIN
                users u 
            ON
                u.id = g.admin_id
            WHERE
                g.id = %(group_id)s
        """
        return self.fetch_one(query, data)

    def update_group_invitation_logs(self, data):
        query = """
            UPDATE
                group_invitation_logs
            SET
                status = %(status)s,
                updated_timestamp = %(updated_timestamp)s
            WHERE
                id = %(group_invitation_logs_id)s
        """
        self.execute_query(query, data)
