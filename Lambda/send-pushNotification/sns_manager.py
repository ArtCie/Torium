import boto3
import json
from content_builder import Content


class SnsManager:
    def __init__(self):
        self.sns = boto3.client(
            service_name='sns',
            region_name='eu-central-1'
        )

    def publish(self, content: Content) -> tuple:
        body = self._get_body_from_content(content)
        response = self.sns.publish(
            TargetArn=content.device_arn,
            Message=json.dumps(body),
            MessageStructure="json"
        )
        response_code = response['ResponseMetadata']['HTTPStatusCode']
        return response_code

    @staticmethod
    def _get_body_from_content(content: Content):
        return {
            "GCM":
                json.dumps(
                    {
                        "notification": {
                            "title": content.title,
                            "body": content.body,
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
                            "title": content.title,
                            "message": content.body,
                            "forward_link": content.forward_link
                        }
                    }
                )
        }

