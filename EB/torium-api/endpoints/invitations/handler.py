from flask import Blueprint
from endpoints.invitations.manager import InvitationsManager

from endpoints.invitations.get.get_invitations_count import GetInvitationsCount
from endpoints.invitations.get.get_invitations import GetInvitations

invitation_handler = Blueprint('invitation', __name__)
invitation_manager = InvitationsManager()


@invitation_handler.route('/groups/invitation/count', methods=['GET'])
def get_count():
    return invitation_manager.handle_request(GetInvitationsCount, payload={})


@invitation_handler.route('/groups/invitation', methods=['GET'])
def get():
    return invitation_manager.handle_request(GetInvitations, payload={})
