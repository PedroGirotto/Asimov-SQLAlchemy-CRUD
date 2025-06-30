from sqlalchemy import String, Boolean, select
from sqlalchemy.orm import Mapped, mapped_column, Session

from src.Base import Base

class Usuario(Base): #representa minha tabela
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __init__(self, nome, senha, email, acesso_gestor):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.acesso_gestor = acesso_gestor

    def __repr__(self):
        return f'Usuario({self.id=}, {self.nome=})'


### CRUD ###
def criar_usuario(
    engine,
    nome:str,
    senha:str,
    email:str,
    acesso_gestor:bool = False
    ):
    with Session(bind = engine) as session:
        usuario = Usuario(nome=nome,senha=senha,email=email,acesso_gestor=acesso_gestor)
        session.add(usuario)
        session.commit()


def ler_todos_usuarios(engine):
    with Session(bind = engine) as session:
        usuarios = session.execute(select(Usuario)).fetchall() 
        return [user[0] for user in usuarios]


def ler_usuario_id(engine, id:int):
    with Session(bind = engine) as session:
        return session.execute(select(Usuario).filter_by(id=id)).fetchall()


def modificar_usuario(
    engine,
    id:int,
    nome=None,
    senha=None,
    email=None,
    acesso_gestor=None
    ):
    with Session(bind=engine) as session:
        usuario = session.execute(select(Usuario).filter_by(id=id)).fetchall()
        for atributos in usuario:
            if nome:
                atributos[0].nome = nome
            if senha:
                atributos[0].senha = senha
            if email:
                atributos[0].email = email
            if acesso_gestor:
                atributos[0].acesso_gestor = acesso_gestor
            
            session.commit()