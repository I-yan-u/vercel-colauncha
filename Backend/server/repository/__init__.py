from server.repository.repository import Repository
from server.models.company import Company
from sqlalchemy.orm import Session


class DBAdaptor:
    def __init__(self, db: Session):
        self.repo = Repository(db, Company)
    