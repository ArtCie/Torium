from flask import Blueprint

groups_members_handler = Blueprint('groups_members', __name__)


@groups_members_handler.route('/group/members', methods=['GET', 'POST'])
def route():
    pass