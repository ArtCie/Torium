from flask import Blueprint

users_handler = Blueprint('users', __name__)


@users_handler.route('/users', methods=['GET', 'POST'])
def route():
    pass