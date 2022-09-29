from flask import Blueprint, request
from endpoints.members.manager import MemberManager

from endpoints.members.post.post_member import PostMember
from endpoints.members.get.get_members import GetMembers
from endpoints.members.patch.status.patch_member_status import PatchMemberStatus
from endpoints.members.patch.role.patch_member_role import PatchMemberRole
from endpoints.members.delete.delete_member import DeleteMember

groups_members_handler = Blueprint('groups_members', __name__)
groups_members_manager = MemberManager()


@groups_members_handler.route('/group/members', methods=['POST'])
def post():
    return groups_members_manager.handle_request(PostMember, payload=request.json)


@groups_members_handler.route('/group/members', methods=['GET'])
def get():
    return groups_members_manager.handle_request(GetMembers, payload=request.args)


@groups_members_handler.route('/group/members', methods=['DELETE'])
def delete():
    return groups_members_manager.handle_request(DeleteMember, payload=request.json)


@groups_members_handler.route('/group/members/status', methods=['PATCH'])
def patch_approve():
    return groups_members_manager.handle_request(PatchMemberStatus, payload=request.json)


@groups_members_handler.route('/group/members/role', methods=['PATCH'])
def patch_role():
    return groups_members_manager.handle_request(PatchMemberRole, payload=request.json)