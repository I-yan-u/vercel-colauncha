from typing import Optional
from fastapi import APIRouter, BackgroundTasks, File, Form, UploadFile
from server.schemas import APIResponse, RequestSchema, ServiceResultModel
from server.utils.exception_handler import ErrorMessage
from server.services.request_form_services import RequestFormServices
import json
import logging
from pydantic import ValidationError

# Configure logging for error tracking
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

routes = APIRouter(prefix="/requests", tags=["Service Requests"])

@routes.post("/form-submit")
async def form_submit(
    background_tasks: BackgroundTasks,
    required_skills: Optional[str] = Form(None),
    estimated_budget: int = Form(...),
    company_name: str = Form(...),
    phone: str = Form(...),
    max_project_time: int = Form(...),
    project_name: str = Form(...),
    country: str = Form(...),
    email: str = Form(...),
    description: str = Form(...),
    attachment: Optional[UploadFile] = File(None),
) -> APIResponse:
    result = ServiceResultModel()
    required_skills = required_skills.split(",")\
        if "," in required_skills and len(required_skills) > 0\
        else required_skills
    file_content = None
    file_name = None
    file_type = None
    allowed_content_types = ["application/pdf", "image/jpeg", "image/png"]
    # # Parse required skills JSON string
    # if required_skills:
    #     try:
    #         parsed_skills = json.loads(required_skills)
    #     except json.JSONDecodeError as e:
    #         error_msg = "Failed to parse 'required_skills'. Invalid JSON format."
    #         logger.error(f"{error_msg}: {e}")
    #         raise ErrorMessage(message=error_msg, status_code=400, detail=e.msg )

    try:
        request_data = RequestSchema(
            required_skills=required_skills,
            estimated_budget=estimated_budget,
            company_name=company_name,
            phone=phone,
            max_project_time=max_project_time,
            project_name=project_name,
            country=country,
            email=email,
            description=description
        )
        request_data = RequestSchema.model_validate(request_data)
    except ValidationError as e:
        logger.error(f"Validation error in request data: {e}")
        raise ErrorMessage(
            status_code=422,
            detail=e.errors(),
            message="Validation error in request data"
        )

    if attachment and attachment.content_type in allowed_content_types:
        try:
            file_name = attachment.filename
            file_type = attachment.content_type
            file_content = await attachment.read()
        except Exception as e:
            error_msg = "Failed to process attachment."
            logger.error(f"{error_msg}: {e}")
            raise ErrorMessage(
                status_code=500,
                detail=error_msg,
                message="Failed to process attachment"
            )
    # RequestFormServices().form_submit(
    # request_data,
    # file_content,
    # file_name, file_type
    # )
    # background_tasks.add_task(RequestFormServices().form_submit, request_data, file_content, file_name, file_type)
    return APIResponse(
        data=result.data,
        message="Request submitted successfully"
    )
