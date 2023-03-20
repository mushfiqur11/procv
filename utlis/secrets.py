import os
from starlette.config import Config
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    
def get_secret_key():
    '''
    This function returns google client id
    '''
    return os.environ['SECRET_KEY']

def get_google_client_id():
    '''
    This function returns google client id
    '''
    return os.environ['GOOGLE_CLIENT_ID']
    

def get_google_client_secret():
    '''
    This function returns google client secret
    '''
    return os.environ['GOOGLE_CLIENT_SECRET']
    
def set_env_variable(keys, env_source = '.env'):
    '''
    This function sets the environment variables from environment secrets
    Takes in key as a parameter and checks if it exists in env source
    '''
    config = Config(env_source)
    config_dict = config.__dict__.get('file_values')
    if type(keys)==str:
        keys = [keys]
    for key in keys:
        if key in config_dict:
            os.environ[key] = config_dict[key]
            logging.info(f'Added {key} to environment variables')
        else:
            logging.info(f'{key} not in provided env file')


