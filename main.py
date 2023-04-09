import logging
import uvicorn
import argparse
from app import *
def start_server(host = "127.0.0.1",port = 8009):
    '''
    The functions starts the FastAPI server in port 8000
    '''
    uvicorn.run("app.app:app", 
                host=host,
                port = port,
                reload=True)

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default="localhost", help="Host address")
    parser.add_argument('--port', type=int, default=8009, help="Host port")
    args = parser.parse_args()

    host = args.host
    port = args.port

    start_server(host,port)