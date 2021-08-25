from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils import cbv
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import schemas
from ...commons.logger_services.logger_factory_service import SrvLoggerFactory
from ...models import crud, database
from ...resources.dependencies import get_db

_logger = SrvLoggerFactory("locations").get_logger()
router = APIRouter()

schemas.Base.metadata.create_all(bind=database.engine)


@cbv.cbv(router)
class Locations:

    @router.post("/locations")
    def create_locations(self, records: Dict, db: Session = Depends(get_db)):
        try:
            _logger.info("create record in for locations")
            db_records = crud.insert_records(db=db, records=records, model="locations")
            return db_records
        except Exception as error:
            _logger.error(f"Error while inserting records in chains :{error}")

    @router.post("/locations/bulk-insert")
    async def create_locations(self, records: List, db: Session = Depends(get_db)):
        try:
            _logger.info("Insert bulk record in for locations")
            crud.bulk_insert_records(db=db, list_records=records, model="locations")
            return {"message": "success"}

        except IntegrityError as error:
            _logger.error(f"Error while inserting records in locations :{error}")
            raise HTTPException(status_code=409, detail=f"Error while trying to save data {error}")

        except Exception as error:
            _logger.error(f"Error while inserting records in locations :{error}")
            raise HTTPException(status_code=500, detail="Error while trying to save data")

    @router.get("/locations")
    async def get_locations(self, db: Session = Depends(get_db)):
        try:
            db_records = crud.get_records(db=db, model="locations")
            return db_records
        except Exception as error:
            _logger.error(f"Error while fetching records in chains :{error}")

    @router.delete("/locations/{name}")
    async def delete_locations(self, name: str, db: Session = Depends(get_db)):
        try:
            db_records = crud.delete_record(db=db, model="locations", value=name, column_name="chain")
            if db_records:
                return {"message": "success"}
        except Exception as error:
            _logger.error(f"Error while deleting records in products :{error}")
            raise HTTPException(status_code=500, detail=f"Error while trying to delete data {error}")