from sqlalchemy import String, Boolean, select
from sqlalchemy.orm import Mapped, mapped_column, Session

from src.Base import Base


class Usuario(Base): #representa minha tabela
    '''
    Descrição: Classe que representa a tabela usuarios no banco de dados PostgreSQL. Herda de Base, a base declarativa do SQLAlchemy.

    Atributos:
        __tablename__: Nome da tabela no banco: 'usuarios'.
        id: Chave primária do tipo int.
        nome: Nome do usuário (String(30)).
        senha: Senha do usuário (String(30)).
        email: Email do usuário (String(30)).
        acesso_gestor: Booleano que indica se o usuário tem acesso de gestor.
    '''

    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)


    def __init__(self, nome, senha, email, acesso_gestor):
        '''
        Descrição: Inicializa um novo objeto Usuario com os dados fornecidos.

        Parâmetros:
            nome (str): Nome do usuário.
            senha (str): Senha do usuário.
            email (str): Email do usuário.
            acesso_gestor (bool): Define se o usuário é gestor (padrão: False).
        '''

        self.nome = nome
        self.senha = senha
        self.email = email
        self.acesso_gestor = acesso_gestor


    def __repr__(self):
        '''
        Descrição: Retorna uma representação legível do objeto Usuario, útil para depuração.
        '''

        return f'Usuario({self.id=}, {self.nome=})'


### CRUD ###
def criar_usuario(
    engine,
    nome:str,
    senha:str,
    email:str,
    acesso_gestor:bool = False
    ):
    '''
    Descrição: Cria um novo usuário na tabela usuarios.

    Parâmetros:
        engine: Conexão com o banco de dados.
        nome (str): Nome do novo usuário.
        senha (str): Senha do usuário.
        email (str): Email do usuário.
        acesso_gestor (bool): Indica se o usuário terá acesso de gestor (default: False).
    '''

    with Session(bind = engine) as session:
        usuario = Usuario(nome=nome,senha=senha,email=email,acesso_gestor=acesso_gestor)
        session.add(usuario)
        session.commit()


def ler_todos_usuarios(engine):
    '''
    Descrição: Lê todos os registros da tabela usuarios.

    Parâmetro:
        engine: Conexão com o banco de dados.

    Retorno:
        List[Usuario]: Lista de objetos Usuario.
    '''
    
    with Session(bind = engine) as session:
        usuarios = session.execute(select(Usuario)).fetchall() 
        return [user[0] for user in usuarios]


def ler_usuario_id(engine, id:int):
    '''
    Descrição: Busca um usuário específico com base no seu id.

    Parâmetros:
        engine: Conexão com o banco de dados.
        id (int): ID do usuário.

    Retorno:
        List[Usuario]: Lista contendo o usuário (ou vazia se não encontrado).
    '''

    with Session(bind = engine) as session:
        return session.execute(select(Usuario).filter_by(id=id)).fetchall()


def modificar_usuario(
    engine,
    id:int,
    **kwargs 
    ):
    '''
    Descrição: Modifica os atributos de um usuário com base em argumentos passados dinamicamente.

    Parâmetros: 
        engine: Conexão com o banco de dados.
        id (int): ID do usuário a ser modificado.
        **kwargs: Dicionário com os nomes e valores dos campos a serem atualizados.
        
        Valores possíveis da kwargs:
            nome (str): Novo nome do usuário.
            senha (str): Nova senha.
            email (str): Novo email.
            acesso_gestor (bool): Atualiza o status de acesso de gestor (True ou False).
    '''

    with Session(bind=engine) as session:
        usuario = session.execute(select(Usuario).filter_by(id=id)).fetchall()
        for atributos in usuario:
            for key, value in kwargs.items():
                setattr(usuario[0], key, value)
            
        session.commit()