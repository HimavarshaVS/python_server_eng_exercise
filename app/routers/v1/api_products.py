from typing import Dict, List
from fastapi_pagination import Page, Params, paginate
from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi_utils import cbv
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ...models.base_models import *
from app.models import schemas
from ...commons.logger_services.logger_factory_service import SrvLoggerFactory
from ...models import crud, database
from ...resources.dependencies import get_db

_logger = SrvLoggerFactory("products").get_logger()
router = APIRouter()

schemas.Base.metadata.create_all(bind=database.engine)


@cbv.cbv(router)
class ProductsAPI:

    @router.post("/products", summary="Insert single record for product")
    def create_products(self, records: CreateProductPost, db: Session = Depends(get_db)):
        try:
            _logger.info("create record in for chains")
            db_records = crud.insert_records(db=db, records=records, model="products")
            return db_records
        except Exception as error:
            _logger.error(f"Error while inserting records in chains :{error}")

    @router.post("/products/bulk-insert", summary="Insert bulk records for products")
    async def create_chains(self, records: List, db: Session = Depends(get_db)):
        try:
            _logger.info("create record in for chains")
            crud.bulk_insert_records(db=db, list_records=records, model="products")
            return {"message": "success"}

        except IntegrityError as error:
            _logger.error(f"Error while inserting records in chains :{error}")
            raise HTTPException(status_code=409, detail=f"Error while trying to save data {error}")

        except Exception as error:
            _logger.error(f"Error while inserting records in chains :{error}")
            raise HTTPException(status_code=500, detail="Error while trying to save data")

    @router.get("/products", summary="List all products")
    async def get_products(self, params: Params = Depends(), db: Session = Depends(get_db)):
        try:
            db_records = crud.get_records(db=db, model="products")
            return paginate(db_records, params)
        except Exception as error:
            _logger.error(f"Error while fetching records in chains :{error}")

    @router.get("/products/{product}", summary="List a product and associated chains")
    def get_products_associated_chains(self, product: str, response: Response, db: Session = Depends(get_db)):
        try:
            db_rec_products = crud.get_records_based_on_val(db=db, model="products", column_name="product", value=product)

            if len(db_rec_products) == 0:
                _logger.error(f"No records found for product : {product}")
                response.status_code = 204
                return {"message": f"No records found for product : {product}"}
            product_details = db_rec_products[0].__dict__
            del product_details['_sa_instance_state']

            chains = []
            if not len(product_details['chains']) == 0:
                for chain in product_details['chains']:
                    db_rec_chains = crud.get_records_based_on_val(db=db, model="chains", column_name="name",
                                                                    value=chain)
                    if not len(db_rec_chains) == 0:
                        chain_details = db_rec_chains[0].__dict__
                        del chain_details['_sa_instance_state']
                        chains.append(chain_details)
            product_details['chains'] = chains
            return product_details

        except Exception as error:
            _logger.error(f"Error while fetching records in products :{error}")
            return {"message": f"Error while fetching records : {error}"}

    @router.delete("/products/{name}", summary="Delete a product based on product name")
    async def delete_chain(self, name: str, db: Session = Depends(get_db)):
        try:
            db_records = crud.delete_record(db=db, model="products", value=name, column_name="product")
            if db_records:
                return {"message": "success"}
        except Exception as error:
            _logger.error(f"Error while deleting records in products :{error}")
            raise HTTPException(status_code=500, detail=f"Error while trying to delete data {error}")
