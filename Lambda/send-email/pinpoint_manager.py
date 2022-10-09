import boto3
from secret_manager import SecretManager


class PinpointManager:
    def __init__(self, secret_manager: SecretManager):
        self.pinpoint = boto3.client(
            service_name='pinpoint',
            region_name='eu-central-1'
        )
        self.APP_ID = secret_manager.get_pinpoint_app_id()
        self.SENDER = "arturciesielczyk1@gmail.com"
        self.CHAR_SET = "UTF-8"

    def create_send_email_event(self, email: str, message: str) -> None:
        html_message = self._format_html(message)
        self.pinpoint.send_messages(
            ApplicationId=self.APP_ID,
            MessageRequest={
                'Addresses': {
                    email: {'ChannelType': 'EMAIL'}
                },
                'MessageConfiguration': {
                    'EmailMessage': {
                        'FromAddress': self.SENDER,
                        'SimpleEmail': {
                            'Subject': {'Charset': self.CHAR_SET, 'Data': "Torium reminder"},
                            'HtmlPart': {'Charset': self.CHAR_SET, 'Data': html_message},
                            'TextPart': {'Charset': self.CHAR_SET, 'Data': message}}}}})

    @staticmethod
    def _format_html(message: str):
        first_row = message[:message.find('!') + 1]
        last_row = message[message.find('!') + 1:]
        return f"""
        <html>
            <head></head>
            <body>
                <h2>{first_row}</h2>
                <p>{last_row}</p>
            </body>
        </html>
        """
