import logging
import uvicorn
import argparse
from app import *
def start_server():
    '''
    The functions starts the FastAPI server in port 8000
    '''
    uvicorn.run("app.app:app", 
                # host= "https://localhost/",
                port = 8000,
                reload=True)

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--new_db', type=bool, default=False, help="Initiate new dataset. Set true if no dataset exists")
    # args = parser.parse_args()

    start_server()