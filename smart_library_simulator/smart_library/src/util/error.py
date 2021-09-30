class InvalidInputError(Exception):
    """Error to be thrown when the client provided an input that was not
    understood by the smartlibrary (e.g. non-existing attribute used,
    non-existent context selected etc.)"""

    def __init__(self, description):
        self.description = description


class NotFoundError(Exception):
    """Error to be thrown when the client provided an input for which no
    resource was found by the smartlibrary"""

    def __init__(self, description):
        self.description = description
