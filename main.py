from sqlalchemy import create_engine, URL
from src.Base import Base

url_object = URL.create(
    'postgresql+psycopg2',
    username = 'postgre', # UTILIZAR arquivo conf para não colocar info no git
    password = 'LandOfPostgre7&', # UTILIZAR arquivo conf para não colocar info no git
    host = 'localhost', # UTILIZAR arquivo conf para não colocar info no git
    port = 5432,
    database = 'asimov_sqlalchemy_project', # UTILIZAR arquivo conf para não colocar info no git
)


engine = create_engine(url_object, echo=True)
Base.metadata.create_all(bind=engine)