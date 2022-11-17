from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def post_event_comment(self, data):
        query = """
            INSERT INTO
                events_comments
            (   
                event_id,
                user_id,
                comment,
                timestamp
            )
            VALUES
            (
                %(event_id)s,
                %(user_id)s,
                %(comment)s,
                %(timestamp)s
            )
            RETURNING
            id
        """
        return self.fetch_one(query, data)

    def get_events_comments(self, data):
        query = """
            SELECT
                id,
                user_id,
                comment,
                timestamp as event_timestamp
            FROM
                events_comments
            WHERE
                event_id = %(event_id)s
            ORDER BY
                timestamp DESC
        """
        return self.fetch_all(query, data)

    def update_event_comment(self, data):
        query = """
            UPDATE
                events_comments
            SET
                comment = %(comment)s
            WHERE 
                id = %(id)s
        """
        return self.execute_query(query, data)

    def delete_event_comment(self, data):
        query = """
            DELETE FROM
                events_comments
            WHERE
                id = %(id)s
            AND
                user_id = %(user_id)s
            RETURNING id
        """
        return self.fetch_one(query, data)

    def valid_user_comment_relation(self, data):
        query = """
            SELECT
                1
            FROM
                events_comments
            WHERE
                user_id = %(user_id)s
            AND 
                id = %(id)s
        """
        return self.fetch_one(query, data)

    def valid_user_event_relation(self, data):
        query = """
            SELECT
                1
            FROM
                events_users
            WHERE
                user_id = %(user_id)s
            AND 
                event_id = %(event_id)s
        """
        return self.fetch_one(query, data)