from flask import Blueprint

connections_handler = Blueprint('connections', __name__)


@connections_handler.route('/connections', methods=['GET', 'POST'])
def route():
    pass