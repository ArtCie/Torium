from flask import Blueprint, request
from endpoints.users.manager import UsersManager

from endpoints.users.patch.patch_user_preferences import PatchUserPreferences
from endpoints.users.patch.patch_user_mobile import PatchUserMobile
from endpoints.users.patch.patch_user_organization import PatchUserOrganization
from endpoints.users.post.post_user_mobile import PostUserMobile
from endpoints.users.get.get_user import GetUser

users_handler = Blueprint('users', __name__)
users_manager = UsersManager()


@users_handler.route('/users', methods=['GET'])
def get_user():
    return users_manager.handle_request(GetUser, payload={})

@users_handler.route('/users/preferences', methods=['PATCH'])
def patch_preferences():
    return users_manager.handle_request(PatchUserPreferences, payload=request.json)


@users_handler.route('/users/mobile', methods=['POST'])
def post_mobile():
    return users_manager.handle_request(PostUserMobile, payload=request.json)


@users_handler.route('/users/mobile', methods=['PATCH'])
def patch_mobile():
    return users_manager.handle_request(PatchUserMobile, payload=request.json)

@users_handler.route('/users/organization', methods=['PATCH'])
def patch_organization():
    return users_manager.handle_request(PatchUserOrganization, payload=request.json)