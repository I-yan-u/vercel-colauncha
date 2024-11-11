from uuid import UUID
from pydantic import BaseModel, Field
from server.configs import app_configs


class GetCompanySchema(BaseModel):
    id: UUID = Field(
        description="Unique identifier for the company"
    )
    name: str = Field(
        description="Name of the company",
        examples=["Company Name"]
    )
    country: str = Field(
        description="Country where the company is located",
        examples=["Nigeria"]
    )
    phone: str = Field(
        description="Phone number of the company",
        examples=["08012345678"]
    )
    email: str = Field(
        description="Email of the company",
        examples=["email@example.com"]
    )


class CompanyLoginSchema(BaseModel):
    email: str = Field(
        min_length=3, max_length=255, examples=[app_configs.test_company.COMPANY_NAME]
    )
    password: str = Field(
        min_length=8, max_length=128, examples=[app_configs.test_company.PASSWRD]
    )


class RegisterCompanySchema(GetCompanySchema):
    password: str = Field(
        description="Password for the company account",
        examples=[app_configs.test_company.PASSWRD]
    )

    model_config = {
        "orm_mode": True,
        "from_attributes": True
    }


class LoginToken(BaseModel):
    access_token: str
    token_type: str