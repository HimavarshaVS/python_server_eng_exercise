from sqlalchemy.orm import Session
from ..models.schemas import Chains


from ..commons.logger_services.logger_factory_service import SrvLoggerFactory

_logger = SrvLoggerFactory("crud").get_logger()


def insert_records(db: Session, records):
    _logger.info("Inserting records in chains")
    db_records = Chains(**records)
    db.add(db_records)
    db.commit()
    db.refresh(db_records)
    return db_records


def get_records(db: Session):
    return db.query(Chains)

