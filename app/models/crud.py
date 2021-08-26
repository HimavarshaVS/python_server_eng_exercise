from sqlalchemy.orm import Session
from ..models.schemas import *


from ..commons.logger_services.logger_factory_service import SrvLoggerFactory

_logger = SrvLoggerFactory("crud").get_logger()


def insert_records(db: Session, records, model):
    _logger.info(f"Inserting records in {model}")
    if model == 'chains':
        db_records = Chains(**records)
    elif model == 'products':
        db_records = Products(**records)
    else:
        db_records = Locations(**records)
    db.add(db_records)
    db.commit()
    db.refresh(db_records)
    return db_records


def get_records(db: Session, model):
    model_val = get_model(model)
    _logger.info(f"Fetch all records from {model_val}")
    return db.query(model_val).all()


def get_records_based_on_val(db: Session, model, column_name, value):
    model_val = get_model(model)
    _logger.info(f"Fetching records for {value} from {model_val}")
    query = db.query(model_val)
    sql = {column_name: value}
    query = query.filter_by(**sql)
    return query.all()


def bulk_insert_records(db: Session, list_records, model):
    model_val = get_model(model)
    _logger.info(f"Bulk insert in {model_val}")
    db.bulk_insert_mappings(model_val, [dict(rec) for rec in list_records], return_defaults=True)
    db.commit()


def delete_record(db: Session, model, column_name, value):
    model_val = get_model(model)
    _logger.info(f"Deleting record for {value} in {model_val}")

    query = db.query(model_val)
    sql = {column_name: value}
    query.filter_by(**sql).delete()
    db.commit()

    return True


def get_model(group):
    models_dict = {"chains": Chains,
                   "products": Products,
                   "locations": Locations}

    return models_dict.get(group)



