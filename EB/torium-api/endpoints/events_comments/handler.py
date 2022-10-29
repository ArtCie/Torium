from flask import Blueprint, request
from endpoints.events_comments.manager import EventCommentManager

from endpoints.events_comments.post.post_event_comment import PostEventComment
from endpoints.events_comments.get.get_event_comments import GetEventComments
from endpoints.events_comments.put.put_event_comment import PutEventComment
from endpoints.events_comments.delete.delete_event_comment import DeleteEventComment

events_comments_handler = Blueprint('events_comments', __name__)
event_comment_manager = EventCommentManager()


@events_comments_handler.route('/event/comment', methods=['POST'])
def post():
    return event_comment_manager.handle_request(PostEventComment, payload=request.json)


@events_comments_handler.route('/event/comment', methods=['GET'])
def get():
    return event_comment_manager.handle_request(GetEventComments, payload={})


@events_comments_handler.route('/event/comment', methods=['PUT'])
def put():
    return event_comment_manager.handle_request(PutEventComment, payload=request.json)


@events_comments_handler.route('/event/comment', methods=['DELETE'])
def delete():
    return event_comment_manager.handle_request(DeleteEventComment, payload=request.json)
