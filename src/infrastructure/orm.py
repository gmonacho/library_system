import os
from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base: Any = declarative_base()


db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_name = os.getenv("DB_NAME")
db_password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}",
    echo=True,
    future=True,
)
