from flask import Blueprint
from endpoints.organizations.manager import OrganizationManager

from endpoints.organizations.get.get_organizations import GetOrganizations

organizations_handler = Blueprint('organizations', __name__)
groups_members_manager = OrganizationManager()


@organizations_handler.route('/organizations', methods=['GET'])
def get():
    return groups_members_manager.handle_request(GetOrganizations, payload={})