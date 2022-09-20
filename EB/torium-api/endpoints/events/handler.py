from flask import Blueprint

events_handler = Blueprint('events', __name__)


@events_handler.route('/events', methods=['GET', 'POST'])
def route():
    pass