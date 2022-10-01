from database.db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def get_organizations(self):
        query = """
            SELECT
                name,
                url,
                file_name
            FROM
                organizations
        """
        return self.fetch_all(query, {})
