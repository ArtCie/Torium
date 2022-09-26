from flask import Blueprint, request
from endpoints.members.manager import MemberManager

from endpoints.members.post.post_member import PostMember
from endpoints.members.get.get_member import GetMember
from endpoints.members.patch.status.patch_member_status import PatchMemberStatus
from endpoints.members.patch.approve.patch_member_approve import PatchMemberApprove
from endpoints.members.delete.delete_member import DeleteMember

groups_members_handler = Blueprint('groups_members', __name__)
groups_members_manager = MemberManager()


@groups_members_handler.route('/group/members', methods=['POST'])
def post():
    return groups_members_manager.handle_request(PostMember, payload=request.json)


@groups_members_handler.route('/group/members', methods=['GET'])
def get():
    return groups_members_manager.handle_request(GetMember, payload=request.args)


@groups_members_handler.route('/group/members', methods=['DELETE'])
def delete():
    return groups_members_manager.handle_request(DeleteMember, payload=request.json)


@groups_members_handler.route('/group/members/approve', methods=['PATCH'])
def put_approve():
    return groups_members_manager.handle_request(PatchMemberApprove, payload=request.json)


@groups_members_handler.route('/group/members/status', methods=['PATCH'])
def put_status():
    return groups_members_manager.handle_request(PatchMemberStatus, payload=request.json)