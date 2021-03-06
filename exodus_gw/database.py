from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import get_settings

# The database name is identical to the user name
SQLALCHEMY_DATABASE_URL = (
    "postgresql://{s.db_service_user}:{s.db_service_pass}@"
    "{s.db_service_host}:{s.db_service_port}/{s.db_service_user}"
).format(s=get_settings())
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
