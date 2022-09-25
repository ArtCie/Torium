from flask import Flask
from flask_cors import CORS
from endpoints.users.handler import users_handler
from endpoints.events.handler import events_handler
from endpoints.groups.handler import groups_handler
from endpoints.members.handler import groups_members_handler
from endpoints.organization.handler import organizations_handler

api = Flask(__name__)
api.register_blueprint(users_handler)
api.register_blueprint(events_handler)
api.register_blueprint(groups_handler)
api.register_blueprint(groups_members_handler)
api.register_blueprint(organizations_handler)

cors = CORS(
    api,
    resources={
        r"/*": {
            "origins": "*"
        }
    }
)

if __name__ == '__main__':
    api.run(host='0.0.0.0', debug=False)
