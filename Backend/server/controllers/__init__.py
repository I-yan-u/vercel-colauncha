"""Controllers"""

from fastapi import APIRouter
from server.configs import app_configs
from server.controllers import Request_controller
# from server.schemas import BadRequest, NotFound, ServerError


router = APIRouter(prefix=app_configs.API_VERSION)

router.include_router(Request_controller.routes)