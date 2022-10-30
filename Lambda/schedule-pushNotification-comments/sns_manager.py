import boto3
import json


class SnsManager:
    def __init__(self):
        self.sns = boto3.client(
            service_name='sns',
            region_name='eu-central-1'
        )

    def publish(self, title: str, body: str, device_arn: str, event_id: str) -> tuple:
        body = self._get_body_from_content(title, body, event_id)
        response = self.sns.publish(
            TargetArn=device_arn,
            Message=json.dumps(body),
            MessageStructure="json"
        )
        response_code = response['ResponseMetadata']['HTTPStatusCode']
        return response_code

    @staticmethod
    def _get_body_from_content(title: str, body: str, event_id: str):
        return {
            "GCM":
                json.dumps(
                    {
                        "notification": {
                            "title": title,
                            "body": body,
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
                            "title": title,
                            "message": body,
                            "event_id": event_id
                        }
                    }
                )
        }

