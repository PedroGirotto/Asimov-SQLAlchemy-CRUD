import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, URL
from src.Base import Base

load_dotenv()

url_object = URL.create(
    drivername = 'postgresql+psycopg2',
    username = os.getenv('login'),
    password = os.getenv('password'),
    host = os.getenv('host'),
    port = int(os.getenv('port'), 10),
    database = os.getenv('database'),
)


engine = create_engine(url_object, echo=True)
Base.metadata.create_all(bind=engine)