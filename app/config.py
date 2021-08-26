
class ConfigClass(object):
    version = "0.1.0"

    RDS_HOST = "192.168.0.31"
    RDS_PORT = 5432
    RDS_DBNAME = "data"
    RDS_USER = "varsha"
    RDS_PWD = "admin"
    SQLALCHEMY_DATABASE_URL = f"postgresql://{RDS_USER}:{RDS_PWD}@{RDS_HOST}/{RDS_DBNAME}"
