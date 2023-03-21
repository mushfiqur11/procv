from fastapi import FastAPI, Depends, HTTPException
import logging
from models.database import get_engine
from models import schemas, models
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional
from starlette.middleware.sessions import SessionMiddleware
from controllers import google, facebook, amazon
from starlette.requests import Request
from app import modules



logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="!secret")

def get_db():
    engine = get_engine('procv')
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/users/', response_model=List[schemas.User])
async def get_users(limit: int = 100, db: Session = Depends(get_db)):
    users = modules.get_users(limit=limit, db=db)
    return users

@app.get('/users/{user_id}', response_model=schemas.User)
async def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
    user = modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post('/users/', response_model=Optional[schemas.UserBase])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    email = user.email
    if not models.User.is_valid_email(email):
        raise HTTPException(status_code=400, detail="Invalid email address")
    db_user = modules.get_user_by_email(email=email,db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = modules.get_user_by_username(username=user.username, db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return modules.create_user(user=user, db=db)

### CONTACTS

@app.get('/contacts/{user_id}',response_model=List[schemas.Contact])
async def get_contacts_by_user(user_id: int, db: Session=Depends(get_db)):
    return modules.get_contacts_by_user(user_id,db)

@app.get('/contacts/{user_id}/{contact_type}',response_model=List[schemas.Contact])
async def get_contacts_by_user_and_type(user_id: int, contact_type:str, db: Session=Depends(get_db)):
    return modules.get_contacts_by_user_and_type(user_id,contact_type,db)

@app.post('/contacts/',response_model=schemas.Contact)
async def create_contact(contact: schemas.ContactCreate, db: Session= Depends(get_db)):
    return modules.create_contact(contact,db)

### PROJECTS

@app.get('/projects/{user_id}', response_model=List[schemas.Project])
async def get_projects_by_user(user_id: int, db: Session=Depends(get_db)):
    return modules.get_projects_by_user(user_id,db)

@app.get('/projects/{user_id}/{project_type}', response_model=List[schemas.Project])
async def get_projects_by_user_and_type(user_id: int, project_type:str, db: Session=Depends(get_db)):
    return modules.get_projects_by_user_and_type(user_id,project_type,db)

@app.post('/projects/', response_model=schemas.Project)
async def create_project(project: schemas.ProjectCreate, db: Session= Depends(get_db)):
    return modules.create_project(project, db)

### EXPERIENCES

@app.get('/experiences/{user_id}', response_model = List[schemas.Experience])
async def get_experiences_by_user(user_id: int, db: Session=Depends(get_db)):
    return modules.get_experiences_by_user(user_id,db)

@app.get('/experiences/{user_id}/{exp_type}', response_model = List[schemas.Experience])
async def get_experiences_by_user_and_type(user_id: int, exp_type:str, db: Session=Depends(get_db)):
    return modules.get_experiences_by_user_and_type(user_id,exp_type,db)

@app.post('/experiences/', response_model=schemas.Experience)
async def create_experience(experience: schemas.ExperienceCreate, db: Session= Depends(get_db)):
    return modules.create_experience(experience,db)

### ACCOLADES

@app.get('/accolades/{user_id}', response_model = List[schemas.Accolade])
async def get_accolades_by_user(user_id: int, db: Session = Depends(get_db)):
    return modules.get_accolades_by_user(user_id, db)

@app.post('/accolades/', response_model=schemas.Accolade)
async def create_accolade(accolade: schemas.AccoladeCreate, db: Session= Depends(get_db)):
    return modules.create_accolade(accolade,db)


### BLOGS

@app.get('/blogs/', response_model = List[schemas.Blog])
async def get_blogs(db: Session= Depends(get_db)):
    return modules.get_blogs(db)

@app.get('/blogs/{user_id}', response_model = List[schemas.Blog])
async def get_blogs_by_user(user_id: int, db: Session= Depends(get_db)):
    return modules.get_blogs_by_user(user_id,db)

@app.post('/blogs/', response_model=schemas.Blog)
async def create_blog(blog: schemas.BlogCreate, db: Session= Depends(get_db)):
    return modules.create_blog(blog,db)


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



