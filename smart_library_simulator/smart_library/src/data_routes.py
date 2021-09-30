import logging
import os
import urllib

from flask import Blueprint, Response, jsonify, request
from models.dbmodels import Fragrance
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from util.error import NotFoundError

from smart_library.src.global_state import GlobalState
from smart_library.src.processors.curation_processor import CurationProcessor


def _build_database_connection_string() -> str:
    user_name = urllib.parse.quote_plus(
        os.environ.get("FRAGRANCEDB_USERNAME", "")
    )
    password = urllib.parse.quote_plus(
        os.environ.get("FRAGRANCEDB_PASSWORD", "")
    )
    host = os.environ.get("FRAGRANCEDB_HOST", "")
    port = os.environ.get("FRAGRANCEDB_PORT", "")
    db_name = os.environ.get("FRAGRANCEDB_NAME", "")
    extra_info = os.environ.get("FRAGRANCEDB_EXTRA", "?")

    db_url = (
        "postgresql://"
        f"{user_name}:{password}@{host}:{port}/{db_name}{extra_info}"
    )

    return db_url


GlobalState.db_connection_string = _build_database_connection_string()
GlobalState.engine = create_engine(GlobalState.db_connection_string)
GlobalState.db_session_maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=GlobalState.engine
)

Base = declarative_base()

GlobalState.curation_processor = CurationProcessor(
    GlobalState.db_session_maker
)


logger = logging.getLogger(__name__)
main_endpoints = Blueprint("main_endpoints", __name__)
data_endpoints = Blueprint("data_endpoints", __name__)


@main_endpoints.route("/curation", methods=["POST"])
def curate():
    return Response("my curation!", 200)


@main_endpoints.route("/")
def teapot():
    return Response("I'm the smart library!", 200)


@data_endpoints.route("/fragrances", methods=["GET"])
def fragrances() -> Response:
    with GlobalState.session_scope() as db_session:
        data = db_session.query(Fragrance).all()
        return jsonify({"data": data})


@data_endpoints.route("/fragrance/<id>", methods=["GET"])
def single_fragrance(
    id: str,
) -> Response:

    result = {}
    with GlobalState.session_scope() as db_session:
        try:
            result = (
                db_session.query(Fragrance)
                .filter_by(fragrance_id=id)
                .first()
            )
        except Exception:
            db_session.rollback()
        return jsonify(result)
