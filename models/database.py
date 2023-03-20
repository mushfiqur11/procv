from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

username = 'root'
password = 'Mra180317'
host = 'localhost'
# database_name = ''

def create_new_db(database_name):
    '''
    This function creates a new database in the server and returns engine and the sessionlocal
    '''
    DATABASE_URL = f"mysql://{username}:{password}@{host}"
    engine = create_engine(DATABASE_URL)
    with engine.connect() as con:
        # schema_old = con.execute(text(f"SELECT '{cred.schema}' FROM information_schema.schemata WHERE schema_name = '{cred.schema}';")).fetchone() is not None
        con.execute(text(f"CREATE SCHEMA IF NOT EXISTS {database_name};"))
        # schema_exists = con.execute(text(f"SELECT '{cred.schema}' FROM information_schema.schemata WHERE schema_name = '{cred.schema}';")).fetchone() is not None
    Base.metadata.create_all(engine)
    return None

def get_engine(database_name):
    '''
    This function checks if a database already exists
    '''
    DATABASE_URL = f"mysql://{username}:{password}@{host}/{database_name}"
    create_new_db(database_name)
    engine = create_engine(DATABASE_URL)
    return engine