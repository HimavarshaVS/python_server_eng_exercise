from fastapi_sqlalchemy import db
from sqlalchemy import Column, String, Date, DateTime, Integer, Boolean, ForeignKey, Float
# from sqlalchemy.ext.declarative import declarative_base
from app.config import ConfigClass
from .database import Base
from sqlalchemy.sql import func
from datetime import datetime

from ..commons.logger_services.logger_factory_service import SrvLoggerFactory

_logger = SrvLoggerFactory("schemas").get_logger()


class Chains(Base):
    __tablename__ = "chains"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String())
    image_url = Column(String())
    created = Column(DateTime, server_default=func.now(), nullable=False)
    modified = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    country = Column(String())
    online_store = Column(String())  # can you boolean value instead


class Locations(Base):
    __tablename__ = "locations"
    # Chain latitude longitude Postal code enabled Phone
    id = Column(Integer, unique=True, primary_key=True)
    chain = Column(String())
    latitude = Column(Float())
    longitude = Column(Float())
    postal_code = Column(Integer())
    enabled = Column(String())
    phone = Column(Integer())


class Products(Base):
    __tablename__ = "products"
    # Product name Product URL Cost Chains
    id = Column(Integer, unique=True, primary_key=True)
    product = Column(String())
    product_url = Column(String())
    cost = Column(Float())
    chains = Column(String())
