import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_sqlalchemy_database_uri():
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    server = "postgresql"
    db_name = "mev_inspect"
    return f"postgresql://{username}:{password}@{server}/{db_name}"


def get_engine():
    return create_engine(get_sqlalchemy_database_uri())


def get_session():
    Session = sessionmaker(bind=get_engine())
    return Session()
