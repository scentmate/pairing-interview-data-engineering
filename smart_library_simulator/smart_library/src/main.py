import logging

from flask import Flask, jsonify

from smart_library.src.data_routes import data_endpoints, main_endpoints
from smart_library.src.util.error import InvalidInputError, NotFoundError
from smart_library.src.util.json_encoder import SmartlibraryEncoder

api = Flask(__name__)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


api.register_blueprint(data_endpoints)
api.register_blueprint(main_endpoints)

# Apply custom JSON encoder that gives deserialization control to classes
api.json_encoder = SmartlibraryEncoder


@api.errorhandler(NotFoundError)
def handle_not_found_error(e):
    return (
        jsonify(
            {
                "error": "NotFoundError",
                "description": e.description,
            }
        ),
        404,
    )


@api.errorhandler(InvalidInputError)
def handle_invalid_input_error(e):
    return (
        jsonify(
            {
                "error": "InvalidInputError",
                "description": e.description,
            }
        ),
        400,
    )


if __name__ == "__main__":
    logger.info("--- SCENTMATE SMARTLIBRARY SERVICE: Startup ---")

    api.run(
        host='0.0.0.0',
        port=9099
    )
