from endpoints.organizations.db_manager import DBManager
from endpoints.organizations.content import ContentConverter
from endpoints.organizations.get.organizations_builder import OrganizationsBuilder


class GetOrganizations:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self.organizations_builder = OrganizationsBuilder()

    def process_request(self) -> dict:
        organizations = self._get_organizations()
        parsed_organizations = self._parse_organizations(organizations)
        return self.organizations_builder.build_organizations_response(parsed_organizations)

    def _get_organizations(self) -> list:
        return self._db_manager.get_organizations()

    @staticmethod
    def _parse_organizations(organizations: list) -> list:
        return [ContentConverter.convert(row) for row in organizations]
