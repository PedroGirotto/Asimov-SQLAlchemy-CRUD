from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, Session

from src.Base import Base

class Usuario(Base):
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
def criar_usuario(engine,nome:str,senha:str,email:str,acesso_gestor:bool = False):
    with Session(bind = engine) as session:
        usuario = Usuario(nome=nome,senha=senha,email=email,acesso_gestor=acesso_gestor)
        session.add(usuario)
        session.commit()