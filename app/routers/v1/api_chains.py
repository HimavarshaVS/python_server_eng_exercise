from fastapi import APIRouter, Depends
from typing import Dict
from fastapi.responses import StreamingResponse
from fastapi_utils import cbv
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db
from fastapi_pagination import PaginationParams, Page
from fastapi_pagination.paginator import paginate
from app.models import schemas
from ...resources.dependencies import get_db
from ...models import crud, database

from ...commons.logger_services.logger_factory_service import SrvLoggerFactory

_logger = SrvLoggerFactory("crud").get_logger()
router = APIRouter()

schemas.Base.metadata.create_all(bind=database.engine)


@cbv.cbv(router)
class Chains:

    @router.post("/chains", tags=["V1"],
                 summary="Create chains")
    async def create_chains(self, records: Dict, db: Session = Depends(get_db)):
        try:
            _logger.info("create record in for chains")
            db_records = crud.insert_records(db=db, records=records)
            return db_records
        except Exception as error:
            _logger.error(f"Error while inserting records in chains :{error}")

    @router.get("/chains")
    async def get_chains(self, db: Session = Depends(get_db)):
        try:
            db_records = crud.get_records(db=db)
            return db_records
        except Exception as error:
            _logger.error(f"Error while fetching records in chains :{error}")
