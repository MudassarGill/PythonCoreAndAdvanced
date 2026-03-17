# # main.py
# from fastapi import FastAPI
# import logging

# #logging setup

# logging.basicConfig(
#     level=logging.INFO,
#     )
# logger=logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# file_handler=logging.FileHandler('modules.log')
# file_handler.setLevel(logging.INFO)
# console_handler=logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)

# app = FastAPI()

# logger.info('FastAPI started')

# @app.get("/")
# def read_root():
#     logger.info('FastAPI root endpoint')
#     return {"message": "Hello, FastAPI!"}

# logger.info('FastAPI path parameters endpoint')

# @app.get("/item/{item_id}")
# def read_item(item_id: int):
#     logger.info('FastAPI path parameters endpoint')
#     return {"item_id": item_id}

# logger.info('FastAPI query parameters endpoint')

# @app.get("/search/")
# def search_items(query: str, page: int = 1, page_size: int = 10):
#     return {
#         "query": query,
#         "page": page,
#         "page_size": page_size,
#         "results": [f"{query}_result_{i}" for i in range(page_size)]
#     }



from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # Pydantic model
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None  # Optional field

# # POST endpoint with request body
# @app.post("/items/")
# def create_item(item: Item):
#     return {"item_name": item.name, "item_price": item.price, "offer": item.is_offer}



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(
    level=logging.INFO,
    )
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler('fastapi.log')
file_handler.setLevel(logging.INFO)
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


app=FastAPI()
logger.info('FastAPI started basemodel')

class Item(BaseModel):
    name:str
    price:float
    is_offer:bool=None



item={}

logger.info('Database file created')
@app.post("/items/")


def create_item(item:Item):
    logger.info('Item created')
    return {"item_name":item.name,"item_price":item.price,"offer":item.is_offer}

logger.info('Get endpoint created')
@app.get("/items/{item_id}")
def read_item(item_id:int):
    logger.info('Item read')
    return item[item_id]

logger.info('Put endpoint created')
@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    logger.info('Item updated')
    if item_id not in item:
        raise HTTPException(status_code=404,detail="Item not found")
    item[item_id]=item
    return item[item_id]

logger.info('Delete endpoint created')
@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    logger.info('Item deleted')
    if item_id not in item:
        raise HTTPException(status_code=404,detail="Item not found")
    del item[item_id]
    return {"message":"Item deleted"}

