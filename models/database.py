from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from models.models import Base
from starlette.config import Config

config = Config('.env')
config_dict = config.__dict__.get('file_values')

username = str(config_dict['username'])
password = str(config_dict['password'])
host = str(config_dict['database_host'])
# database_name = ''

# db = 'MongoDB'
# db = 'SQL'
db = 'Cockroach'

def create_new_db(database_name):
    '''
    This function creates a new database in the server and returns engine and the sessionlocal
    '''
    TempBase = declarative_base()

    if db=='MongoDB':
        # DATABASE_URL = f"mongodb+srv://{username}:{password}@{host}"
        DATABASE_URL = DATABASE_URL = f"mongodb:///?Server={host}&Port=27017&User={username}&Password={password}"
    elif db=='SQL':
        DATABASE_URL = f"mysql://{username}:{password}@{host}"
    elif db=='Cockroach':
        password = str(config_dict['COCKROACH_PASSWORD'])
        username = str(config_dict['COCKROACH_USER'])
        DATABASE_URL= f"cockroachdb://{username}:{password}@chasm-gorilla-10098.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
    
    engine = create_engine(DATABASE_URL)
    with engine.connect() as con:
        # schema_old = con.execute(text(f"SELECT '{cred.schema}' FROM information_schema.schemata WHERE schema_name = '{cred.schema}';")).fetchone() is not None
        con.execute(text(f"CREATE SCHEMA IF NOT EXISTS {database_name};"))
        # schema_exists = con.execute(text(f"SELECT '{cred.schema}' FROM information_schema.schemata WHERE schema_name = '{cred.schema}';")).fetchone() is not None
    TempBase.metadata.create_all(engine)
    return None

def get_engine(database_name = 'mrahma45$default'):
    '''
    This function returns a database engine if it already exists. Has support for MongoDB, MySQL, and CockroachDB. 
    '''
    if db == 'MongoDB':
        # DATABASE_URL = f"mongodb+srv://{username}:{password}@{host}/{database_name}"
        DATABASE_URL = f"mongodb:///?Server={host}&Port=27017&Database={database_name}&User={username}&Password={password}"
    elif db=='SQL':
        DATABASE_URL = f"mysql://{username}:{password}@{host}/{database_name}"
    elif db=='Cockroach':
        password = str(config_dict['COCKROACH_PASSWORD'])
        username = str(config_dict['COCKROACH_USER'])
        DATABASE_URL= f"cockroachdb://{username}:{password}@chasm-gorilla-10098.7tt.cockroachlabs.cloud:26257/{database_name}?sslmode=verify-full"
    
    create_new_db(database_name)
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine 
