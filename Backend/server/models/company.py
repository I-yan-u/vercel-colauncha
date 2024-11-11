from sqlalchemy.orm import relationship
from sqlalchemy import Column,  String
from server.models.base import ModelBase
from passlib.context import CryptContext


class Company(ModelBase):
    __tablename__ = "company"
    __mapper_args__ = {"polymorphic_identity": "company"}
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    requests = relationship("Request", back_populates="company")

    def __init__(
            self,
            name: str,
            country: str,
            phone: str,
            email: str,
            password: str
        ) -> None:
        self.name = name
        self.country = country
        self.phone = phone
        self.email = email
        self.password = self.__hash_password(password)
    
    def __hash_password(self, password) -> str:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)