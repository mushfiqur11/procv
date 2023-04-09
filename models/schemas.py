from typing import List, Optional
import uuid
from pydantic import BaseModel, validator
from datetime import date

class UserBase(BaseModel):
    full_name: Optional[str] = None
    pronouns: Optional[str] = None
    username: str
    email: str
    profile_img: Optional[str] = None
    thumb_img: Optional[str] = None
    cover_img: Optional[str] = None
    bio: Optional[str] = None
    career_role: Optional[str] = None
    # template: Optional[str] = None
    
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str


class User(UserBase):
    _id: str
    verified: bool
    summary: Optional[str]

    # @validator('_id')
    # def validate_uuid(cls, value):
    #     try:
    #         uuid.UUID(value)
    #     except ValueError:
    #         raise ValueError('Invalid UUID')
    #     return value
    
    class Config:
        orm_mode = True

class UserSecured(BaseModel):
    _user_id: str
    _secured_id: str
    user_info: User
    email: str
    hashed_password: str
    salt: str

    class Config:
        orm_mode = True

class ContactBase(BaseModel):
    contact_value: str
    visible: bool = True
    contact_type: str
    thumb_img: Optional[str] = None
    thumb_txt: Optional[str] = None

    class Config:
        orm_mode = True

class ContactCreate(ContactBase):
    _user_id: str

    class Config:
        orm_mode = True

class Contact(ContactBase):
    _contact_id: str

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    project_type: str
    title: str
    sub_heading: Optional[str] = None
    short_desc: Optional[str] = None
    long_desc: Optional[str] = None
    tags: Optional[str] = None
    thumb_img: Optional[str] = None
    main_img: Optional[str] = None
    other_media: Optional[str] = None
    other_media_title: Optional[str] = None
    code: Optional[str] = None
    paper: Optional[str] = None
    app: Optional[str] = None
    other_link: Optional[str] = None
    other_link_title: Optional[str] = None


class ProjectCreate(ProjectBase):
    _user_id: str
    visible: bool = True


class Project(ProjectBase):
    _project_id: str

    class Config:
        orm_mode = True


class ExperienceBase(BaseModel):
    experience_type: str
    title: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    position: Optional[str] = None
    role: Optional[str] = None
    desc: Optional[str] = None
    image: Optional[str] = None
    employer: Optional[str] = None
    employer_link: Optional[str] = None
    supervisor: Optional[str] = None
    supervisor_link: Optional[str] = None


class ExperienceCreate(ExperienceBase):
    _user_id: str
    visible: bool = True


class Experience(ExperienceBase):
    _experience_id: str

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    title: str
    sub_heading: Optional[str] = None
    thumb_img: Optional[str] = None
    tags: Optional[str] = None
    text: Optional[str] = None


class BlogCreate(BlogBase):
    _user_id: str
    visible: bool = True


class Blog(BlogBase):
    _blog_id: str

    class Config:
        orm_mode = True


class AccoladeBase(BaseModel):
    title: str
    date: Optional[str] = None
    position: Optional[str] = None
    role: Optional[str] = None
    desc: Optional[str] = None
    image: Optional[str] = None
    provider: Optional[str] = None
    provider_link: Optional[str] = None


class AccoladeCreate(AccoladeBase):
    _user_id: str
    visible: bool = True


class Accolade(AccoladeBase):
    _accolade_id: str

    class Config:
        orm_mode = True


class SkillBase(BaseModel):
    skill_name: str

    class Config:
        orm_mode = True

class SkillCreate(SkillBase):
    _user_id: str

    class Config:
        orm_mode = True

class Skill(SkillBase):
    _skill_id: str

    class Config:
        orm_mode = True


class Submit(BaseModel):
    username: str
    password: str
    name: Optional[str] = None
    email: str
    phone: Optional[str]
    github: Optional[str]
    city: Optional[str] = None
    profileImg: Optional[str] = None
    coverImg: Optional[str] = None
    thumbnailImg: Optional[str] = None
    bio: Optional[str] = None
    projects: Optional[List[ProjectCreate]] =None
    education: Optional[List[ExperienceCreate]] = None
    experience: Optional[List[ExperienceCreate]] = None
    skills: Optional[List[SkillCreate]] = None



class About(BaseModel):
    name: str
    email: str
    bio: str
    phone: str
    github: str
    city: str

    class Config:
        orm_mode = True
