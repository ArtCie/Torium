from flask import Blueprint, request
from endpoints.events.manager import EventManager

from endpoints.events.delete.delete_event import DeleteEvent
from endpoints.events.post.post_event import PostEvent
from endpoints.events.get.get_events import GetEvents
from endpoints.events.put.put_event import PutEvent
from endpoints.events.post.post_notify_event import PostNotifyEvent

events_handler = Blueprint('events', __name__)
event_manager = EventManager()


@events_handler.route('/event', methods=['POST'])
def post():
    return event_manager.handle_request(PostEvent, payload=request.json)


@events_handler.route('/event', methods=['GET'])
def get():
    return event_manager.handle_request(GetEvents, payload=request.args)


@events_handler.route('/event', methods=['PUT'])
def put():
    return event_manager.handle_request(PutEvent, payload=request.json)


@events_handler.route('/event', methods=['DELETE'])
def delete():
    return event_manager.handle_request(DeleteEvent, payload=request.json)


@events_handler.route('/event/notify', methods=['POST'])
def post_notify():
    return event_manager.handle_request(PostNotifyEvent, payload=request.json)