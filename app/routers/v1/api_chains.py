import json
from typing import Dict, List

from sqlalchemy.exc import IntegrityError

import psycopg2
from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi_utils import cbv
from sqlalchemy.orm import Session

from ...models import schemas
from ...models.schemas import *
from ...commons.logger_services.logger_factory_service import SrvLoggerFactory
from ...models import crud, database
from ...resources.dependencies import get_db

_logger = SrvLoggerFactory("crud").get_logger()
router = APIRouter()

schemas.Base.metadata.create_all(bind=database.engine)


@cbv.cbv(router)
class ChainsAPI:

    @router.post("/chains",
                 summary="Create chains")
    async def create_chains(self, records: Dict, db: Session = Depends(get_db)):
        try:
            _logger.info("create record in for chains")
            db_records = crud.insert_records(db=db, records=records, model="chains")
            return db_records
        except Exception as error:
            _logger.error(f"Error while inserting records in chains :{error}")

    @router.post("/chains/bulk")
    async def create_chains(self, records: List, db: Session = Depends(get_db)):
        try:
            _logger.info("create record in for chains")
            crud.bulk_insert_records(db=db, list_records=records, model="chains")
            return {"message": "success"}

        except IntegrityError as error:
            _logger.error(f"Error while inserting records in chains :{error}")
            raise HTTPException(status_code=409, detail=f"Error while trying to save data {error}")

        except Exception as error:
            _logger.error(f"Error while inserting records in chains :{error}")
            raise HTTPException(status_code=500, detail="Error while trying to save data")

    @router.get("/chains")
    async def get_chains(self, db: Session = Depends(get_db)):
        try:
            db_records = crud.get_records(db=db, model="chains")
            return db_records
        except Exception as error:
            _logger.error(f"Error while fetching records in chains :{error}")

    @router.get("/chains/{name}")
    async def get_chain_associated_loc(self, name: str,  response: Response, db: Session = Depends(get_db)):
        try:
            db_rec_chains = crud.get_records_based_on_val(db=db, model="chains", column_name="name", value=name)

            if len(db_rec_chains) == 0:
                _logger.error(f"No records found for chain : {name}")
                response.status_code = 204
                return {"message": f"No records found for chain : {name}"}
            chain_details = db_rec_chains[0].__dict__
            del chain_details['_sa_instance_state']

            # get corresponding locations
            db_rec_loc = crud.get_records_based_on_val(db=db, model="locations", column_name="chain", value=name)
            locations = []
            if len(db_rec_loc) > 0:
                for record in db_rec_loc:
                    record = record.__dict__
                    del record['_sa_instance_state']
                    del record['id']
                    locations.append(record)
            chain_details['locations'] = locations
            return chain_details

        except Exception as error:
            _logger.error(f"Error while fetching records in chains :{error}")
            return {"message": f"Error while fetching records : {error}"}

    @router.delete("/chains/{name}")
    async def delete_chain(self, name: str, response: Response, db: Session = Depends(get_db)):
        try:
            db_records = crud.delete_record(db=db, model="chains", value=name, column_name="name")
            if db_records:
                return {"message": "success"}
        except Exception as error:
            _logger.error(f"Error while deleting records in chains :{error}")
            raise HTTPException(status_code=500, detail=f"Error while trying to delete data {error}")