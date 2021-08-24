from ..models.database import SessionLocal
from ..commons.logger_services.logger_factory_service import SrvLoggerFactory

_logger = SrvLoggerFactory("dependencies").get_logger()


def get_db():
    _logger.info("Connecting db")
    db = SessionLocal()
    try:
        yield db
    finally:
        _logger.info("Closing db connection")
        db.close()
