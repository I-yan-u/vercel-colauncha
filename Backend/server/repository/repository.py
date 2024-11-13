from sqlalchemy.orm import Session
from server.models.company import Company
from server.models.base import ModelBase
from server.schemas.Company_schema import GetCompanySchema


class Repository:
    """Store access"""
    def __init__(self, db: Session, model: Company) -> None:
        self.db = db
        self._Model = model
    
    async def add(self, data: dict) -> GetCompanySchema:
        """Adds an object of type self._Model to db"""
        try:
            entity = self._Model(**data)
            self.db.add(entity)
            self.db.commit()
            self.db.refresh(entity)
            return GetCompanySchema.model_validate(entity.to_dict())
        except Exception as e:
            self.db.rollback()
            raise e

    async def get_by_id(self, id: str) -> GetCompanySchema:
        """Get db entry by id"""
        try:
            result = self.db.query(self._Model).filter_by(id=id).first()
            result = GetCompanySchema.model_validate(result)
            return result if result else None
        except Exception as e:
             raise e
    
    async def get_by_email(self, email: str) -> Company:
        """Get db entry by id"""
        try:
            result = self.db.query(
                self._Model
            ).filter_by(email=email).first()
            return result if result else None
        except Exception as e:
             raise e
        
    async def update(
            self,
            entity: GetCompanySchema,
            data: dict = None
        ) -> GetCompanySchema:
        """Updates entity"""
        try:
            ent = self.db.query(self._Model).filter_by(id=entity.id).first()
            if data:
                for k, v in data.items():
                    setattr(ent, k, v)
            self.db.commit()
            self.db.refresh(ent)
            return GetCompanySchema.model.validate(ent)
        except Exception as e:
            raise e
        
    async def delete(self, entity: ModelBase) -> bool:
        """Delete entity from db"""
        try:
            self.db.delete(entity)
            self.db.commit()
        except Exception as e:
            raise e
        return True
    
    async def get_all():
        ...