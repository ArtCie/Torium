from flask import request, jsonify
from database.db_manager_base import DBManagerBase


class EndpointManager:
    def process_request(self, endpoint_class, db_manager: DBManagerBase, **kwargs):
        payload = self._add_headers_to_payload(kwargs['payload'])
        endpoint = endpoint_class(payload, db_manager)
        return endpoint.process_request()

    @staticmethod
    def _add_headers_to_payload(kwargs):
        headers = {header_key[4:].replace('-', '_').lower(): header_value for (header_key, header_value)
                   in request.headers.items()
                   if header_key.lower().startswith('trm')}
        return {**kwargs, **headers}

    @staticmethod
    def _build_response(code, message, data):
        return jsonify(
            {
                "status": {
                    "code": code,
                    "message": message
                },
                "data": data
            }
        )
