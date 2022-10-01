from utils.logger import log_exception, log
from database.secret_manager import SecretManager

from endpoints.endpoint_manager import EndpointManager
from endpoints.organizations.db_manager import DBManager


class OrganizationManager(EndpointManager):
    @log
    def handle_request(self, endpoint_class, **kwargs):
        database = self._get_database()
        try:
            database.connect()
            result = self.process_request(endpoint_class, database, **kwargs)
            database.commit_changes()
            return self._build_response(200, "Success", result)
        except Exception as e:
            log_exception(type(self).__name__, str(e))
            database.rollback_changes()
            return self._build_response(404, "Something went wrong", None)
        finally:
            database.close_database()

    @staticmethod
    def _get_database():
        secret_manager = SecretManager()
        db_config = secret_manager.get_db_config()
        return DBManager(db_config)
