import random
import uvicorn

from fastapi import FastAPI, Body
from fastapi_utils.tasks import repeat_every
from pydantic import BaseModel
from sqlalchemy.orm import Session

from cms.src.infrastructure.api.routes import routes
from cms.src.infrastructure.logging import logger
from cms.src.infrastructure.orm.sqlalchemy import SessionLocal, engine, Base
from cms.src.application.fragrances import modify_fragrance
from cms.src.application.notification import notify

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "cms-endpoints",
        "description": "Operations with the cms",
    },
]

app = FastAPI(
    title="Content-too CMS",
    openapi_tags=tags_metadata
)
db = SessionLocal()

listener = None

app.include_router(routes)


class HostListener(BaseModel):
    host: str
    port: int
    endpoint: str

listener_example = {
  "host": "http://smart_library",
  "port": 9099,
  "endpoint": "/notifications"
}

@app.post("/listener", tags=["cms-endpoints"])
async def add_listener(
    listener_value: HostListener = Body(..., example=listener_example)
):
    global listener
    listener = f"{listener_value.host}:{listener_value.port}{listener_value.endpoint}"
    logger.info(f"New listener {listener}")
    return {"Listener added"}

@app.delete("/listener", tags=["cms-endpoints"])
async def remove_listener():
    global listener
    listener = None
    return {"Removed added"}

@app.on_event("startup")
@repeat_every(seconds=20 + random.randint(0, 5))
def modify_some_entry() -> None:
    global listener
    logger.info("------Updating the data--------")
    delta = modify_fragrance(db)
    logger.info(f"Available listener => {listener}")
    notify(delta, listener)
    logger.info("------Data modified----------")


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=9090,
        log_level="info",
        workers=1
    )