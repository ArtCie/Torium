from flask import Blueprint, request
from endpoints.groups.manager import GroupManager

from endpoints.groups.delete.delete_group import DeleteGroup
from endpoints.groups.post.post_group import PostGroup
from endpoints.groups.get.get_group import GetGroups
from endpoints.groups.put.put_group import PutGroup


groups_handler = Blueprint('groups', __name__)
groups_manager = GroupManager()


@groups_handler.route('/groups', methods=['POST'])
def post():
    return groups_manager.handle_request(PostGroup, payload=request.json)


@groups_handler.route('/groups', methods=['GET'])
def get():
    return groups_manager.handle_request(GetGroups, payload=request.args)


@groups_handler.route('/groups', methods=['PUT'])
def put():
    return groups_manager.handle_request(PutGroup, payload=request.json)


@groups_handler.route('/groups', methods=['DELETE'])
def delete():
    return groups_manager.handle_request(DeleteGroup, payload=request.json)
