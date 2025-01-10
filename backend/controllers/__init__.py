"""Controllers"""

from fastapi import APIRouter
from ..configs import app_configs
from .request_controller import routes


router = APIRouter(prefix=app_configs.API_VERSION)

router.include_router(routes)
