import logging

logger = logging.getLogger(__name__)


class CurationProcessor:
    def __init__(self, session_maker):
        self.session_maker = session_maker
        pass
