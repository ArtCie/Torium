from flask import Blueprint

organizations_handler = Blueprint('organizations', __name__)


@organizations_handler.route('/organizations', methods=['GET', 'POST'])
def route():
    pass