# main.py
from fastapi import FastAPI
import logging

#logging setup

logging.basicConfig(
    level=logging.INFO,
    )
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler('modules.log')
file_handler.setLevel(logging.INFO)
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

app = FastAPI()

logger.info('FastAPI started')

@app.get("/")
def read_root():
    logger.info('FastAPI root endpoint')
    return {"message": "Hello, FastAPI!"}

logger.info('FastAPI path parameters endpoint')

@app.get("/item/{item_id}")
def read_item(item_id: int):
    logger.info('FastAPI path parameters endpoint')
    return {"item_id": item_id}