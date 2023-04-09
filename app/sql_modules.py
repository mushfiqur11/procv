from sqlalchemy.orm import Session, sessionmaker
from models.database import get_engine
from models import models,schemas
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
from utils.secrets import get_secret_key
import bcrypt
from datetime import datetime, timedelta

# from  import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

algorithm = 'HS256'

secret_key = get_secret_key()

def hash_password(password, salt):
    return str(bcrypt.hashpw(password,salt))

def get_db():
    engine = get_engine('defaultdb')
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

######################



####################


# # Generate JWT token
# def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
#     return encoded_jwt

# # Verify JWT token
# def decode_access_token(token: str):
#     try:
#         decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
#         return decoded_token
#     except JWTError:
#         return None

# # Authenticate user against database
# def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.username==username).first()
#     if not user:
#         return False
#     user_secured = db.query(models.UserSecured).filter(models.UserSecured._user_id == user._id).first()
#     if not user_secured:
#         return False
#     called_hash = hash_password(password,user_secured.salt)
#     if not (user_secured.hashed_password == called_hash):
#         return False
#     return user



#######################

# Function to get all users
def get_users(limit: int = 100, db: Session = Depends(get_db)) -> List[models.User]:
    users = db.query(models.User).limit(limit).all()
    return users

# async def get_current_user_oauth2(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     try:
#         token_data = decode_access_token(token)
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
#     user = db.query(models.User).filter(models.User.username == token_data.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return user

# # def verify_user(user: schemas.User):


# # Function to get the current active user based on JWT
# def get_current_active_user(current_user: schemas.User = Depends(get_current_user_oauth2)):
#     if not current_user.verified:
#         raise HTTPException(status_code=400, detail="Unverified user")
#     return current_user

# Function to get user by id
def get_user_by_id(user_id: str, db: Session = Depends(get_db)) -> Optional[models.User]:
    user = db.query(models.User).filter(models.User._id == user_id).first()
    return user

# Function to get user by email
def get_user_by_email(email: str, db: Session = Depends(get_db)) -> Optional[models.User]:
    try:
        user = db.query(models.User).filter(models.User.email == email).first()
        return user
    except Exception as e:
        db.rollback()
        print(e)
    return None

# Function to get user by username
def get_user_by_username(username: str, db: Session = Depends(get_db)) -> Optional[models.User]:
    try:
        print(f'user:{username}')
        user = db.query(models.User).filter(models.User.username == username).first()
        print(user._id)
        return user
    except Exception as e:
        db.rollback()
        print(e)
    return None

# Function to create a user
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> Optional[models.User]:
    db_user = models.User(
        full_name=user.full_name,
        pronouns=user.pronouns,
        username=user.username,
        email=user.email,
        profile_img=user.profile_img,
        thumb_img=user.thumb_img,
        cover_img=user.cover_img,
        bio=user.bio,
        career_role=user.career_role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    # try:
    #     salt = bcrypt.gensalt()
    #     password = user.password.encode('utf-8')
    #     db_user_secured = models.UserSecured(
    #         _user_id = db_user._id,
    #         user_info = db_user,
    #         username = db_user.username,
    #         hashed_password = hash_password(password,salt),
    #         salt = salt
    #     )
    #     db.add(db_user_secured)
    #     db.commit()
    #     db.refresh(db_user_secured)
    #     return db_user
    # except:
    #     db.remove(db_user)
    #     db.commit()
    #     db.refresh(db_user)
    #     return None
    


def get_contacts_by_user(_user_id: str,  db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    contacts = db.query(models.Contact).filter(models.Contact._user_id == user._id).limit(limit).all()
    return contacts

def get_contacts_by_user_and_type(_user_id: str, type:str, db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    contacts = db.query(models.Contact).filter(models.Contact._user_id == user._id).filter(models.Contact.contact_type==type).filter(models.Contact.visible==True).limit(limit).all()
    return contacts

def create_contact(contact: schemas.ContactCreate, user_id: str, db: Session = Depends(get_db)):
    # try:
    db_contact = models.Contact(
        visible = contact.visible,
        contact_value = contact.contact_value,
        contact_type = contact.contact_type,
        thumb_img = contact.thumb_img,
        thumb_txt = contact.thumb_txt,
        _user_id = user_id
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


# ### Project

def get_projects_by_user(_user_id: str,  db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    projects = db.query(models.Project).filter(models.Project._user_id == user._id).limit(limit).all()
    return projects

def get_projects_by_user_and_type(_user_id: str, type:str, db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    projects = db.query(models.Project).filter(models.Project._user_id == user._id).filter(models.Project.project_type==type).filter(models.Project.visible==True).limit(limit).all()
    return projects

def create_project(project: schemas.ProjectCreate, user_id: str,  db: Session = Depends(get_db)):
    # try:
    db_project = models.Project(
        title = project.title,
        project_type = project.project_type,
        tags = project.tags,
        sub_heading = project.sub_heading,
        short_desc = project.short_desc,
        long_desc = project.long_desc,
        thumb_img = project.thumb_img,
        main_img = project.main_img,
        other_media = project.other_media,
        other_media_title = project.other_media_title,
        code = project.code,
        paper = project.paper,
        app = project.app,
        other_link = project.other_link,
        other_link_title = project.other_link_title,
        _user_id = user_id
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


# ### Experience

def get_experiences_by_user(_user_id: str,  db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    experiences = db.query(models.Experience).filter(models.Experience._user_id == user._id).limit(limit).all()
    return experiences

def get_experiences_by_user_and_type(_user_id: str, type:str, db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    experiences = db.query(models.Experience).filter(models.Experience._user_id == user._id).filter(models.Experience.experience_type==type).filter(models.Experience.visible==True).limit(limit).all()
    return experiences

def create_experience(experience: schemas.ExperienceCreate, user_id: str,  db: Session = Depends(get_db)):
    # try:
    # start_date = datetime.strptime(str(experience.start_date, '%Y').date()
    # end_date = datetime.strptime(experience.end_date, '%Y').date()
    db_experience = models.Experience(
        experience_type = experience.experience_type,
        title= experience.title,
        start_date= experience.start_date,
        end_date= experience.end_date,
        position= experience.position,
        role= experience.role,
        desc= experience.desc,
        image= experience.image,
        employer= experience.employer,
        employer_link= experience.employer_link,
        supervisor= experience.supervisor,
        supervisor_link= experience.supervisor_link,
        visible = experience.visible,
        _user_id = user_id,
    )
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience

# ### Accolade

def get_accolades_by_user(_user_id: str,  db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    accolades = db.query(models.Accolade).filter(models.Accolade._user_id == user._id).limit(limit).all()
    return accolades

def create_accolade(accolade: schemas.AccoladeCreate, user_id: str,  db: Session = Depends(get_db)):
    # try:
    db_accolade = models.Accolade(
        title = accolade.title,
        date= accolade.date,
        position= accolade.position,
        role= accolade.role,
        desc= accolade.desc,
        image= accolade.image,
        provider= accolade.provider,
        provider_link= accolade.provider_link,
        _user_id = user_id,
        visible = accolade.visible
    )
    db.add(db_accolade)
    db.commit()
    db.refresh(db_accolade)
    return db_accolade

# ### Blog

def get_blogs(db: Session = Depends(get_db), limit:int = 100):
    blogs = db.query(models.Blog).limit(limit).all()
    return blogs

def get_blogs_by_user(_user_id: str,  db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    blogs = db.query(models.Blog).filter(models.Blog._user_id == user._id).limit(limit).all()
    return blogs

def create_blog(blog: schemas.BlogCreate, user_id: str,  db: Session = Depends(get_db)):
    # try:
    db_blog = models.Blog(
        title = blog.title,
        sub_heading = blog.sub_heading,
        thumb_img = blog.thumb_img,
        tags = blog.tags,
        text = blog.text,
        _user_id = user_id,
        visible = blog.visible
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


### Skill

def get_skills_by_user(_user_id: str,  db: Session = Depends(get_db), limit:int = 100):
    user = get_user_by_id(_user_id,db)
    if user is None:
        return []
    skills = db.query(models.Skill).filter(models.Skill._user_id == user._id).limit(limit).all()
    return skills

def create_skill(skill: schemas.SkillCreate, user_id: str,  db: Session = Depends(get_db)):
    # try:
    db_skill = models.Skill(
        skill_name = skill.skill_name,
        _user_id = user_id
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def get_about_user(_user_id: str, db: Session = Depends(get_db)):
    user = get_user_by_id(_user_id,db)
    phone = db.query(models.Contact).filter(models.Contact._user_id == user._id).filter(models.Contact.contact_type=='PHONE').filter(models.Contact.visible==True).first()
    github = db.query(models.Contact).filter(models.Contact._user_id == user._id).filter(models.Contact.contact_type=='GITHUB').filter(models.Contact.visible==True).first()
    location = db.query(models.Contact).filter(models.Contact._user_id == user._id).filter(models.Contact.contact_type=='LOCATION').filter(models.Contact.visible==True).first()
    if phone is None:
        phone = 'N/A'
    else:
        phone = phone.contact_value
    if github is None:
        github = 'N/A'
    else:
        github = github.contact_value
    if location is None:
        location = 'N/A'
    else:
        location = location.contact_value
    db_about = schemas.About(
        name=user.full_name,
        email=user.email,
        bio=user.bio,
        phone=phone,
        github=github,
        city=location
    )
    return db_about

def update_summary(_user_id: str, summary: str, db: Session = Depends(get_db)):
    user = get_user_by_id(_user_id,db)
    if user:
        setattr(user,'summary',summary)
        db.commit()
        db.refresh(user)

# def generate_summary():
