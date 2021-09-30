from fastapi import APIRouter

routes = APIRouter()

@routes.get("/healthcheck", tags=["cms-endpoints"])
async def health_check():
    return {"I am healthy"}

@routes.get("/", tags=["cms-endpoints"])
async def health_check():
    return {"I am a healthy CMS"}
