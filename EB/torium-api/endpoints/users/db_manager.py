from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def get_user(self, data):
        query = """
            SELECT
                u.id as user_id,
                u.username,
                u.email,
                u.mobile_number,
                u.reminder_preferences,
                u.cognito_user_id,
                u.device_arn,
                u.organization_id,
                o.name as organization_name
            FROM
                users u
            LEFT JOIN
                organizations o 
            ON 
                u.organization_id = o.id
            WHERE
                u.id = %(user_id)s
        """
        return self.fetch_one(query, data)

    def update_user_preferences(self, data):
        query = """
            UPDATE
                users
            SET
                reminder_preferences = %(reminder_preferences)s
            WHERE
                id = %(user_id)s
        """
        self.execute_query(query, data)

    def confirm_code(self, data):
        query = """
            UPDATE
                users_verification
            SET
                is_confirmed = %(is_confirmed)s
            WHERE
                user_id = %(user_id)s
            AND 
                code = %(code)s
            RETURNING
                mobile_number
        """
        return self.fetch_one(query, data)

    def update_user_mobile_number(self, data):
        query = """
            UPDATE
                users
            SET
                mobile_number = %(mobile_number)s,
                reminder_preferences = %(reminder_preferences)s
            WHERE
                id = %(user_id)s
        """
        self.execute_query(query, data)

    def init_phone_number(self, data):
        query = """
            INSERT INTO
                users_verification
            (
                user_id, 
                mobile_number, 
                is_sent, 
                is_confirmed, 
                code, 
                timestamp
            )
            VALUES
            (
                %(user_id)s, 
                %(mobile_number)s, 
                %(is_sent)s, 
                %(is_confirmed)s, 
                %(code)s, 
                %(timestamp)s
            )
        """
        self.execute_query(query, data)

    def update_user_organization(self, data):
        query = """
            UPDATE
                users
            SET
                organization_id = %(organization_id)s
            WHERE
                id = %(user_id)s
        """
        self.execute_query(query, data)
