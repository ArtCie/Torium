from aws.sqs_manager import SqsManager
from endpoints.exceptions import InvitationAlreadySent
from endpoints.members.db_manager import DBManager
from endpoints.members.content import ContentConverter


class PostMember:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._content = ContentConverter.convert(kwargs, status='pending')
        self._sqs_manager = SqsManager()
        self.SENT = "sent"
        self.PENDING = "pending"

    def process_request(self):
        self._check_if_invitation_sent()
        group_invitation_logs_id = self._post_member()
        self._create_send_push_group_invitation_event(group_invitation_logs_id)

    def _check_if_invitation_sent(self):
        data = {
            "user_id": self._content.user_id,
            "group_id": self._content.group_id,
            "status_sent": self.SENT,
            "status_pending": self.PENDING
        }
        if self._db_manager.is_invitation_sent(data):
            raise InvitationAlreadySent("Invitation already sent")

    def _post_member(self) -> int:
        data = {
            "group_id": self._content.group_id,
            "user_id": self._content.user_id,
            "status": self._content.status,
            "timestamp": self._content.timestamp
        }
        return self._db_manager.post_member(data)[0]

    def _create_send_push_group_invitation_event(self, group_invitation_logs_id: int) -> None:
        message = {
            "group_invitation_logs_id": {
                "DataType": "String",
                "StringValue": str(group_invitation_logs_id)
            },
            "user_id": {
                "DataType": "String",
                "StringValue": str(self._content.user_id)
            },
            "group_id": {
                "DataType": "String",
                "StringValue": str(self._content.group_id)
            }
        }
        self._sqs_manager.create_send_push_group_invitation_event(message)
