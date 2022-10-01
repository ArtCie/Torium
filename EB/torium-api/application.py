from flask import Flask
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler
from endpoints.users.handler import users_handler
from endpoints.events.handler import events_handler
from endpoints.groups.handler import groups_handler
from endpoints.members.handler import groups_members_handler
from endpoints.organizations.handler import organizations_handler

application = Flask(__name__)
application.register_blueprint(users_handler)
application.register_blueprint(events_handler)
application.register_blueprint(groups_handler)
application.register_blueprint(groups_members_handler)
application.register_blueprint(organizations_handler)

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('/var/log/application.log', maxBytes=1024, backupCount=5)
handler.setFormatter(formatter)
application.logger.addHandler(handler)

cors = CORS(
    application,
    resources={
        r"/*": {
            "origins": "*"
        }
    }
)

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=False)
