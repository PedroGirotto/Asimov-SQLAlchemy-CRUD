import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, URL
from src.Usuario import Usuario, criar_usuario
from src.Base import Base

load_dotenv()

url_object = URL.create(
    drivername = 'postgresql+psycopg2',
    username = os.getenv('LOGIN'),
    password = os.getenv('PASSWORD'),
    host = os.getenv('HOST'),
    port = int(os.getenv('PORT'), 10),
    database = os.getenv('DATABASE')
)


engine = create_engine(url_object, echo=True)
Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    criar_usuario(
        engine,
        nome='Pedro Girotto',
        senha='pedro123456',
        email='pedro.hs.girotto@gmail.com',
        acesso_gestor=True)