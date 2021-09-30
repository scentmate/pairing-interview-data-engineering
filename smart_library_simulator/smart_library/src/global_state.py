from contextlib import contextmanager


class GlobalState:
    engine = None
    db_connection_string = None
    db_session_maker = None

    curation_processor = None
    attribute_recommendation_processor = None

    @staticmethod
    @contextmanager
    def session_scope():
        """Provide a transactional scope around a series of operations."""
        if GlobalState.db_session_maker is None:
            yield None
        else:
            session = GlobalState.db_session_maker()
            try:
                yield session
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
