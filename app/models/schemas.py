from sqlalchemy import Column, String, DateTime, Integer, Float, ARRAY
from sqlalchemy.sql import func

# from sqlalchemy.ext.declarative import declarative_base
from .database import Base
from ..commons.logger_services.logger_factory_service import SrvLoggerFactory

_logger = SrvLoggerFactory("schemas").get_logger()


class Chains(Base):
    __tablename__ = "chains"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(), unique=True)
    image_url = Column(String())
    created = Column(DateTime, server_default=func.now(), nullable=False)
    modified = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    country = Column(String())
    online_store = Column(String())


class Locations(Base):
    __tablename__ = "locations"
    id = Column(Integer, unique=True, primary_key=True)
    chain = Column(String())
    latitude = Column(Float())
    longitude = Column(Float())
    postal_code = Column(String())
    enabled = Column(String())
    phone = Column(String())


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, unique=True, primary_key=True)
    product = Column(String())
    product_url = Column(String())
    cost = Column(Float())
    chains = Column(ARRAY(String))
