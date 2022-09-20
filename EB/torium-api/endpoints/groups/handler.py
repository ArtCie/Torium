from flask import Blueprint

groups_handler = Blueprint('groups', __name__)


@groups_handler.route('/groups', methods=['GET', 'POST'])
def route():
    pass