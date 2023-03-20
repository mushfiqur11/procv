from sqlalchemy.orm import Session, sessionmaker
from models.database import get_engine
from models import models,schemas
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from utils.secrets import get_secret_key
# from  import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

algorithm = 'HS256'

secret_key = get_secret_key()

def get_db():
    engine = get_engine('procv')
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to get all users
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[models.User]:
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# Function to get user by id
def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> Optional[models.User]:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user

async def get_current_user_oauth2(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    user = db.query(models.User).filter(models.User.username == token_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# Function to get the current active user based on JWT
def get_current_active_user(current_user: schemas.User = Depends(get_current_user_oauth2)):
    if not current_user.verified:
        raise HTTPException(status_code=400, detail="Unverified user")
    return current_user

# Function to get user by email
def get_user_by_email(email: str, db: Session = Depends(get_db)) -> Optional[models.User]:
    user = db.query(models.User).filter(models.User.email == email).first()
    return user

# Function to get user by username
def get_user_by_username(username: str, db: Session = Depends(get_db)) -> Optional[models.User]:
    user = db.query(models.User).filter(models.User.username == username).first()
    return user

# Function to create a user
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> models.User:
    db_user = models.User(
        full_name=user.full_name,
        pronouns=user.pronouns,
        username=user.username,
        email=user.email,
        verified=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
