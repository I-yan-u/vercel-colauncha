import json
from typing import Any
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class ErrorMessage(Exception):
    def __init__(self, message: str, status_code: int, detail: str | Any) -> None:
        self.message = message
        self.status_code = status_code
        self.detail = detail


async def error_handler(request: Request, exc: ErrorMessage):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message, "detail": exc.detail, "status_code": exc.status_code},
    )

async def request_validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"message": "Validation error", "detail": str(exc), "status_code": 422},
    )