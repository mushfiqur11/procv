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

@app.post('/users/', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session= Depends(get_db)):
    return {'Data':'Function not implemented'}

### CONTACTS

@app.get('/contacts/', response_model = [schemas.Contact])
async def get_contacts():
    return {'Data':'Function not implemented'}

@app.get('/contacts/{user_id}', response_model = [schemas.Contact])
async def get_contacts_by_user(user: schemas.User):
    return {'Data':'Function not implemented'}

@app.post('/contacts/', response_model=schemas.Contact)
async def create_project(contact: schemas.ContactCreate, db: Session= Depends(get_db)):
    return {'Data':'Function not implemented'}

### PROJECTS

# @app.post('/projects/', response_model=schemas.Project)
# async def create_project(project: schemas.ProjectCreate, db: Session= Depends(get_db)):
#     return {'Data':'Function not implemented'}

@app.get('/projects/', response_model = [schemas.Project])
async def get_projects():
    return {'Data':'Function not implemented'}

@app.get('/projects/{user_id}', response_model = [schemas.Project])
async def get_projects_by_user(user: schemas.User):
    return {'Data':'Function not implemented'}

@app.post('/projects/', response_model=schemas.Project)
async def create_project(project: schemas.ProjectCreate, db: Session= Depends(get_db)):
    return {'Data':'Function not implemented'}

### EXPERIENCES

# @app.post('/experiences/', response_model=schemas.Experience)
# async def create_project(project: schemas.ExperienceCreate, db: Session= Depends(get_db)):
#     return {'Data':'Function not implemented'}

@app.get('/experiences/', response_model = [schemas.Experience])
async def get_experiences():
    return {'Data':'Function not implemented'}

@app.get('/experiences/{user_id}', response_model = [schemas.Experience])
async def get_experiences_by_user(user: schemas.User):
    return {'Data':'Function not implemented'}

@app.post('/experiences/', response_model=schemas.Experience)
async def create_experience(experience: schemas.ExperienceCreate, db: Session= Depends(get_db)):
    return {'Data':'Function not implemented'}

### ACCOLADES

@app.get('/accolades/', response_model = [schemas.Accolade])
async def get_accolades():
    return {'Data':'Function not implemented'}

@app.get('/accolades/{user_id}', response_model = [schemas.Accolade])
async def get_accolades_by_user(user: schemas.User):
    return {'Data':'Function not implemented'}

@app.post('/accolades/', response_model=schemas.Accolade)
async def create_accolade(accolade: schemas.AccoladeCreate, db: Session= Depends(get_db)):
    return {'Data':'Function not implemented'}


### BLOGS

@app.get('/blogs/', response_model = [schemas.Blog])
async def get_blogs():
    return {'Data':'Function not implemented'}

@app.get('/blogs/{user_id}', response_model = [schemas.Blog])
async def get_blogs_by_user(user: schemas.User):
    return {'Data':'Function not implemented'}

@app.post('/blogs/', response_model=schemas.Blog)
async def create_blog(blog: schemas.BlogCreate, db: Session= Depends(get_db)):
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

# @app.get('/login/facebook')
# async def login_facebook():
#     return await facebook.login()

# @app.get('/login/facebook/callback')
# async def get_facebook_user_data():
#     return await facebook.callback()

# # @app.get('/auth/facebook')
# # async def auth_facebook():
# #     return await facebook.callback()

# @app.get('/logout/facebook')
# async def logout_facebook():
#     return {'Data':'Function not implemented'}



