from fastapi.routing import APIRouter

from neo.web.api import document, monitoring, user


api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(user.router)  # Include the user router
api_router.include_router(document.router)  # Include the document router
