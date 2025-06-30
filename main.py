import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, URL
from src.Usuario import *
from src.Base import Base

load_dotenv()

url_object = URL.create(
    drivername = 'postgresql+psycopg2',
    username = os.getenv('LOGIN'),
    password = os.getenv('PASSWORD'),
    host = os.getenv('HOST'),
    port = int(os.getenv('PORT'), 10), # type: ignore
    database = os.getenv('DATABASE')
)


engine = create_engine(url_object, echo=False)
Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    # teste básico das funções

    # criar_usuario(
    #     engine,
    #     nome='Leonardo Maia',
    #     senha='mair_leonardo987123',
    #     email='maia_leonardo@hotmail.com',
    #     acesso_gestor=False)

    #print(ler_todos_usuarios(engine))
    print(ler_usuario_id(engine, 3))
    #modificar_usuario(engine, id=3, email='novo_mail@gmail.com')
    #print(ler_usuario_id(engine, id=3))

    #deletar_usuario(engine, id=2)

    usuario = ler_usuario_id(engine, id=3)
    print(f'Status do login: {usuario.verificar_senha('mair_leonardo987123')}')