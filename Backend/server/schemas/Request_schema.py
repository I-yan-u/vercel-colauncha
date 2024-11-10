from typing import Optional
import pydantic as pyd

class RequestSchema(pyd.BaseModel):
    email: str = pyd.Field(examples=["email@example.com"])
    description: str = pyd.Field(min_length=5,
        max_length=1000, description="Description of the project [1000 characters max]",
        examples=["Description of the project"]
    )
    company_name: str = pyd.Field(
        description="Name of the company",
        examples=["Company Name"]
    )
    estimated_budget: int = pyd.Field(
        examples=[1000000],
        description="Estimated budget for the project (in Naira)"
    )
    country: str = pyd.Field(examples=["Nigeria"])
    phone: str = pyd.Field(examples=["08012345678"])
    project_name: Optional[str] = None
    max_project_time: int = pyd.Field(
        examples=[30],
        description="Maximum time to complete the project (in days)"
    )
    required_skills: Optional[list[str]] = pyd.Field(
        examples=[["Python", "Django", "React"]],
        description="List of required skills for the project"
    )