from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def select_invitations_count(self, data):
        query = """
            SELECT
                count(*)
            FROM
                group_invitation_logs
            WHERE
                user_to = %(user_id)s
            AND
                status = %(status)s
        """
        return self.fetch_one(query, data)

    def select_invitations(self, data):
        query = """
            SELECT
                gil.group_id,
                u.email,
                g.name
            FROM
                group_invitation_logs gil
            INNER JOIN
                groups g 
            ON 
                gil.group_id = g.id
            INNER JOIN
                users u 
            ON 
                u.id = g.admin_id
            WHERE
                gil.user_to = %(user_id)s
            AND
                gil.status = %(status)s
            ORDER BY
                gil.timestamp
            DESC
        """
        return self.fetch_all(query, data)

