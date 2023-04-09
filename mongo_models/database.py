import motor
import pymongo
from starlette.config import Config

config = Config('.env')
config_dict = config.__dict__.get('file_values')

username = str(config_dict['MONGO_username'])
password = str(config_dict['MONGO_password'])
host = str(config_dict['MONGO_host'])

MONGO_URL = f"mongodb+srv://{username}:{password}@h{host}/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URL)

db = client['procv']
user_collection = db['users']
