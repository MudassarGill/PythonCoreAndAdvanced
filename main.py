# from fastapi import FastAPI, HTTPException,status,Depends
# from pydantic import BaseModel
# import logging

# # Logging setup
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler('fastapi.log')
# file_handler.setLevel(logging.INFO)
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)

# FastAPI app
# app = FastAPI()

# logger.info('FastAPI started with BaseModel CRUD')

# # Pydantic model
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None

# In-memory database
# items_db = {}

# # Root endpoint
# @app.get('/')
# def root():
#     logger.info('Root endpoint called')
#     return {'message': 'FastAPI started'}

# # CREATE - POST
# @app.post("/items/{item_id}")
# def create_item(item_id: int, item: Item):
#     if item_id in items_db:
#         raise HTTPException(status_code=400, detail="Item already exists")
#     items_db[item_id] = item
#     logger.info(f'Item {item_id} created')
#     return items_db[item_id]

# READ - GET
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     logger.info(f'Item {item_id} retrieved')
#     return items_db[item_id]

# # UPDATE - PUT
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     items_db[item_id] = item
#     logger.info(f'Item {item_id} updated')
#     return items_db[item_id]

# # DELETE - DELETE
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     del items_db[item_id]
#     logger.info(f'Item {item_id} deleted')
#     return {"message": f"Item {item_id} deleted"}


# app = FastAPI()

# # Dependency function
# token=1234
# def verify_token(token: str):
#     """
#     Token verify karta hai. 
#     Agar valid token nahi hai → HTTPException raise karega
#     """
#     if token != token:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token"
#         )
#     return token
# # Products endpoint
# @app.get("/products/")
# def get_products(token: int = Depends(verify_token)):
#     return {"products": ["Laptop", "Phone", "Tablet"], "user_token": token}

# # Orders endpoint
# @app.post("/orders/")
# def place_order(token: int = Depends(verify_token)):
#     return {"message": "Order placed successfully", "user_token": token}

# # Cart endpoint
# @app.post("/cart/")
# def add_to_cart(token: int = Depends(verify_token)):
#     return {"message": "Item added to cart", "user_token": token}



# from fastapi import FastAPI, HTTPException, status, Depends
# from pydantic import BaseModel,Field,Emailstr
# from typing import Optional


# app=FastAPI()


# class Users(BaseModel):
#     name: str=Field(...,min_length=3,max_length=50)
#     age: Optional[int]=Field(None)
#     email: Emailstr
#     password: int=Field(...,gt=0,min_length=8,max_length=50)

# @app.post('/create-user/')
# def create_user(user: Users):
#     return user



# from fastapi import FastAPI, HTTPException, status, Depends
# from pydantic import BaseModel
# from typing import Optional


# app=FastAPI()

# class UserResponse(BaseModel):
#     name: str
#     email:str
# @app.get('/user',response_model=UserResponse)
# def user_data():
#     return {
#         "name": "Ali",
#         "email": "ali@gmail.com",
#         "password": "123456"
#     }




from fastapi import FastAPI,Form,HTTPException,status

app=FastAPI()

@app.post('/login')
def login(username:str=Form(...),password:str=Form(...)):
    if username=="admin" and password=="admin":
        return {
            "username": username,
            "password": password
    }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

from typing import Optional

app = FastAPI()

@app.post("/login")
def login(username: str = Form(...), remember_me: Optional[bool] = Form(False)):
    return {"username": username, "remember_me": remember_me}