import json
import types


class SmartlibraryEncoder(json.JSONEncoder):
    """Custom JSON encoder"""

    def default(self, object):
        if hasattr(object, "__jsonify__") and isinstance(
            object.__jsonify__, types.MethodType
        ):
            return object.__jsonify__()
        else:  # pragma: no cover
            return json.JSONEncoder.default(self, object)
