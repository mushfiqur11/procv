from fastapi import FastAPI, Depends
import logging
from models.database import get_engine
from models import schemas
from sqlalchemy.orm import sessionmaker, Session
from typing import List
from starlette.middleware.sessions import SessionMiddleware
from controllers import google, facebook, amazon
from starlette.requests import Request



logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="!secret")

def get_db():
    engine = get_engine()
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

### ACCESS OBJECTS (USERS, SHOPS, PRODUCTS)

# @app.get('/')
# async def get_app(request:Request):
#     return await google.homepage(request)

@app.get('/users/', response_model = List[schemas.User])
async def get_users():
    return {'Data':'Function not implemented'}

@app.get('/users/me', response_model = schemas.User)
async def get_current_user():
    return {'Data':'Function not implemented'}

@app.get('/users/{user_id}', response_model = schemas.User)
async def get_user_by_id(user_id:int):
    return {'Data':'Function not implemented'}

@app.get('/shops/', response_model = List[schemas.Shop])
async def get_shops():
    return {'Data':'Function not implemented'}

@app.get('/shops/{shop_id}', response_model = schemas.Shop)
async def get_shop_by_id(shop_id:int):
    return {'Data':'Function not implemented'}

@app.get('/users/{user_id}/shops/', response_model = List[schemas.Shop])
async def get_shops_from_user(user_id:int, db: Session = Depends(get_db)):
    return {'Data':'Function not implemented'}

@app.get('/products/', response_model = List[schemas.Product])
async def get_products():
    return {'Data':'Function not implemented'}

@app.get('/products/{product_id}', response_model = schemas.Product)
async def get_product_by_id(product_id:int):
    return {'Data':'Function not implemented'}

@app.get('/shops/{shop_id}/products/', response_model = List[schemas.Product])
async def get_products_from_shop(shop_id:int):
    return {'Data':'Function not implemented'}

### CREATE NEW OBJECTS (USER, SHOP, PRODUCT)

@app.post('/users/', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session= Depends(get_db)):
    return {'Data':'Function not implemented'}

@app.post('/shops/', response_model=schemas.Shop)
async def create_shop(db: Session = Depends(get_user_by_id)):
    return {'Data':'Function not implemented'}

@app.post('/products/', response_model=schemas.Product)
async def create_product():
    return {'Data':'Function not implemented'}

### ADD FACEBOOK SHOP CREDENTIALS

# @app.post('/users/')


### LOGIN ROUTES (INTERNAL + GOOGLE + FACEBOOK + AMAZON)

@app.get('/login')
async def login():
    return {'Data':'Function not implemented'}

@app.get('/auth')
async def auth():
    return {'Data':'Function not implemented'}

@app.get('/logout')
async def logout():
    return {'Data':'Function not implemented'}

@app.get('/login/google')
async def login_google(request: Request):
    return await google.login(request)

@app.get('/login/google/callback')
async def get_google_user_data(request: Request):
    return await google.callback(request)

# @app.get('/auth/google')
# async def auth_google(request: Request):
#     return await google.auth(request)

@app.get('/logout/google')
async def logout_google(request: Request):
    return await google.logout(request)

@app.get('/login/facebook')
async def login_facebook():
    return await facebook.login()

@app.get('/login/facebook/callback')
async def get_facebook_user_data():
    return await facebook.callback()

# @app.get('/auth/facebook')
# async def auth_facebook():
#     return await facebook.callback()

@app.get('/logout/facebook')
async def logout_facebook():
    return {'Data':'Function not implemented'}

@app.get('/login/amazon')
async def login_amazon():
    return {'Data':'Function not implemented'}

@app.get('/auth/amazon')
async def auth_amazon():
    return {'Data':'Function not implemented'}

@app.get('/logout/amazon')
async def logout_amazon():
    return {'Data':'Function not implemented'}


