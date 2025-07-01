import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, URL

from src.Usuario import * # Base é importado em Usuario
from src.Frontend import *

load_dotenv()

url_object = URL.create(
    drivername = "postgresql+psycopg2",
    username = os.getenv("LOGIN"),
    password = os.getenv("PASSWORD"),
    host = os.getenv("HOST"),
    port = int(os.getenv("PORT"), 10), # type: ignore
    database = os.getenv("DATABASE")
)


engine = create_engine(url_object, echo=False)
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    start_front(engine)