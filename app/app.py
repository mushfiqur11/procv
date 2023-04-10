from fastapi import FastAPI, Depends, HTTPException, Response
import logging
from models.database import get_engine
from models import schemas, models
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional
from starlette.middleware.sessions import SessionMiddleware
from controllers import google, facebook, amazon
from starlette.requests import Request
from app import sql_modules,mongo_modules
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from ai import ai
from mangum import Mangum


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
app = FastAPI()
handler = Mangum(app)

app.add_middleware(SessionMiddleware, secret_key="!secret")


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://example.com",
    "https://example.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    engine = get_engine('defaultdb')
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/users/', response_model=List[schemas.User])
# async def get_users(limit: int = 100, db: Session = Depends(get_db)):
#     users = mongo_modules.get_users(limit=limit, db=db)
#     return users
async def get_users(limit: int = 100, db: Session = Depends(get_db)):
    users = sql_modules.get_users(limit=limit, db=db)
    return users

@app.get('/users/user_id={user_id}', response_model=schemas.User)
# async def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
#     user = mongo_modules.get_user_by_id(user_id, db)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
async def get_user_by_id(user_id:str, db: Session = Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get('/users/username={username}', response_model=schemas.User)
# async def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
#     user = mongo_modules.get_user_by_id(user_id, db)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = sql_modules.get_user_by_username(username, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post('/users/', response_model=Optional[schemas.UserBase])
# async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     email = user.email
#     if not models.User.is_valid_email(email):
#         raise HTTPException(status_code=400, detail="Invalid email address")
#     db_user = mongo_modules.get_user_by_email(email=email,db=db)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     db_user = mongo_modules.get_user_by_username(username=user.username, db=db)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     return mongo_modules.create_user(user=user, db=db)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    email = user.email
    if not models.User.is_valid_email(email):
        raise HTTPException(status_code=400, detail="Invalid email address")
    db_user = sql_modules.get_user_by_email(email=email,db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = sql_modules.get_user_by_username(username=user.username, db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return sql_modules.create_user(user=user, db=db)

### CONTACTS

@app.get('/contacts/user_id={user_id}',response_model=List[schemas.Contact])
# async def get_contacts_by_user(user_id: str, db: Session=Depends(get_db)):
#     return mongo_modules.get_contacts_by_user(user_id,db)
async def get_contacts_by_user(user_id: str, db: Session=Depends(get_db)):
    return sql_modules.get_contacts_by_user(user_id,db)

@app.get('/contacts/user_id={user_id}/{contact_type}',response_model=List[schemas.Contact])
# async def get_contacts_by_user_and_type(user_id: str, contact_type:str, db: Session=Depends(get_db)):
#     return mongo_modules.get_contacts_by_user_and_type(user_id,contact_type,db)
async def get_contacts_by_user_and_type(user_id: str, contact_type:str, db: Session=Depends(get_db)):
    return sql_modules.get_contacts_by_user_and_type(user_id,contact_type,db)

@app.post('/contacts/user_id={user_id}',response_model=schemas.Contact)
# async def create_contact(contact: schemas.ContactCreate, db: Session= Depends(get_db)):
#     return mongo_modules.create_contact(contact,db)
async def create_contact(contact: schemas.ContactCreate, user_id:str, db: Session= Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = user._id
    return sql_modules.create_contact(contact,user_id, db)

### PROJECTS

@app.get('/projects/user_id={user_id}', response_model=List[schemas.Project])
# async def get_projects_by_user(user_id: str, db: Session=Depends(get_db)):
#     return mongo_modules.get_projects_by_user(user_id,db)
async def get_projects_by_user(user_id: str, db: Session=Depends(get_db)):
    return sql_modules.get_projects_by_user(user_id,db)

@app.get('/projects/user_id={user_id}/{project_type}', response_model=List[schemas.Project])
# async def get_projects_by_user_and_type(user_id: str, project_type:str, db: Session=Depends(get_db)):
#     return mongo_modules.get_projects_by_user_and_type(user_id,project_type,db)
async def get_projects_by_user_and_type(user_id: str, project_type:str, db: Session=Depends(get_db)):
    return sql_modules.get_projects_by_user_and_type(user_id,project_type,db)

@app.post('/projects/user_id={user_id}', response_model=schemas.Project)
# async def create_project(project: schemas.ProjectCreate, db: Session= Depends(get_db)):
#     return mongo_modules.create_project(project, db)
async def create_project(project: schemas.Project, user_id:str, db: Session= Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = user._id
    return sql_modules.create_project(project, user_id, db)

### EXPERIENCES

@app.get('/experiences/user_id={user_id}', response_model = List[schemas.Experience])
# async def get_experiences_by_user(user_id: str, db: Session=Depends(get_db)):
#     return mongo_modules.get_experiences_by_user(user_id,db)
async def get_experiences_by_user(user_id: str, db: Session=Depends(get_db)):
    return sql_modules.get_experiences_by_user(user_id,db)

@app.get('/experiences/user_id={user_id}/{exp_type}', response_model = List[schemas.Experience])
# async def get_experiences_by_user_and_type(user_id: str, exp_type:str, db: Session=Depends(get_db)):
#     return mongo_modules.get_experiences_by_user_and_type(user_id,exp_type,db)
async def get_experiences_by_user_and_type(user_id: str, exp_type:str, db: Session=Depends(get_db)):
    return sql_modules.get_experiences_by_user_and_type(user_id,exp_type,db)

@app.post('/experiences/user_id={user_id}', response_model=schemas.Experience)
# async def create_experience(experience: schemas.ExperienceCreate, db: Session= Depends(get_db)):
#     return mongo_modules.create_experience(experience,db)
async def create_experience(experience: schemas.ExperienceCreate, user_id:str, db: Session= Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = user._id
    return sql_modules.create_experience(experience,user_id, db)

### ACCOLADES

@app.get('/accolades/user_id={user_id}', response_model = List[schemas.Accolade])
# async def get_accolades_by_user(user_id: str, db: Session = Depends(get_db)):
#     return mongo_modules.get_accolades_by_user(user_id, db)
async def get_accolades_by_user(user_id: str, db: Session = Depends(get_db)):
    return sql_modules.get_accolades_by_user(user_id, db)

@app.post('/accolades/user_id={user_id}', response_model=schemas.Accolade)
# async def create_accolade(accolade: schemas.AccoladeCreate, db: Session= Depends(get_db)):
#     return mongo_modules.create_accolade(accolade,db)
async def create_accolade(accolade: schemas.AccoladeCreate, user_id:str, db: Session= Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = user._id
    return sql_modules.create_accolade(accolade,user_id, db)


### SKILLS

@app.get('/skills/user_id={user_id}', response_model = List[schemas.Skill])
async def get_skills_by_user(user_id: str, db: Session = Depends(get_db)):
    return sql_modules.get_skills_by_user(user_id, db)

@app.post('/skills/user_id={user_id}', response_model=schemas.Skill)
async def create_skill(skill: schemas.SkillCreate, user_id:str, db: Session= Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = user._id
    return sql_modules.create_skill(skill,user_id, db)

### BLOGS

@app.get('/blogs/', response_model = List[schemas.Blog])
# async def get_blogs(db: Session= Depends(get_db)):
#     return mongo_modules.get_blogs(db)
async def get_blogs(db: Session= Depends(get_db)):
    return sql_modules.get_blogs(db)

@app.get('/blogs/user_id={user_id}', response_model = List[schemas.Blog])
# async def get_blogs_by_user(user_id: str, db: Session= Depends(get_db)):
#     return mongo_modules.get_blogs_by_user(user_id,db)
async def get_blogs_by_user(user_id: str, db: Session= Depends(get_db)):
    return sql_modules.get_blogs_by_user(user_id,db)

@app.post('/blogs/user_id={user_id}', response_model=schemas.Blog)
# async def create_blog(blog: schemas.BlogCreate, db: Session= Depends(get_db)):
#     return mongo_modules.create_blog(blog,db)
async def create_blog(blog: schemas.BlogCreate, user_id:str, db: Session= Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = user._id
    return sql_modules.create_blog(blog,user_id, db)


@app.get('/about/user_id={user_id}', response_model=schemas.About)
async def get_about(user_id:str, db: Session=Depends(get_db)):
    user = sql_modules.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = user._id
    return sql_modules.get_about_user(user_id, db)


@app.post('/submit/', response_model=schemas.Submit)
async def submit(submitResponse: schemas.Submit, db: Session=Depends(get_db)):
    return sql_modules.submit(submitResponse, db)

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

# from weasyprint import HTML, CSS
# from weasyprint.fonts import FontConfiguration

# @app.get('/generate_cv/user_id={user_id}')
# async def generate_cv(job_prompt:str, user_id: str, db: Session=Depends(get_db)):
#     exp_list = sql_modules.get_experiences_by_user(user_id, db)
#     summarized_workexp = ai.get_workexp_summary(exp_list, job_prompt)
#     pdf = ai.generate_pdf(summarized_workexp)
#     try:
#         font_config = FontConfiguration()
#         css = CSS(string='@page { size: A4; margin: 1cm }')
#         pdf = HTML(string=pdf).write_pdf(stylesheets=[css], font_config=font_config)
#         return Response(content=pdf, media_type='application/pdf')
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


