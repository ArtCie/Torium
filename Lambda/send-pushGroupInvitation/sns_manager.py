import boto3
import json
from content_builder import Content


class SnsManager:
    def __init__(self):
        self.sns = boto3.client(
            service_name='sns',
            region_name='eu-central-1'
        )

    def publish(self, device_arn: str, group_data: dict) -> tuple:
        body = self._get_body_from_content(group_data)
        response = self.sns.publish(
            TargetArn=device_arn,
            Message=json.dumps(body),
            MessageStructure="json"
        )
        response_code = response['ResponseMetadata']['HTTPStatusCode']
        return response_code

    @staticmethod
    def _get_body_from_content(group_data: dict):
        return {
            "GCM":
                json.dumps(
                    {
                        "notification": {
                            "title": f"{group_data['name']} - Group invitation",
                            "body": f"From {group_data['email']}",
                        },
                        "android": {
                            "priority": "high",
                            "notification": {
                                "sound": "default"
                            }
                        },
                        "apns": {
                            "payload": {
                                "aps": {
                                    "contentAvailable": True,
                                    "sound": "default"
                                }
                            },
                            "headers": {
                                "apns-push-type": "background",
                                "apns-priority": "5",
                                "apns-topic": "io.flutter.plugins.firebase.messaging"
                            }
                        },
                        "data": {
                            "event": "group_invitation"
                        }
                    }
                )
        }

