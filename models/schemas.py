from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    full_name: Optional[str] = None
    pronouns: Optional[str] = None
    username: str
    email: str
    profile_img: Optional[str] = None
    thumb_img: Optional[str] = None
    cover_img: Optional[str] = None

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    verified: bool

    class Config:
        orm_mode = True

class UserSecured(BaseModel):
    user_id: int
    secured_id: int
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
    user_id: int

    class Config:
        orm_mode = True

class Contact(ContactBase):
    contact_id: int

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
    user_id: int
    visible: bool = True


class Project(ProjectBase):
    project_id: int

    class Config:
        orm_mode = True


class ExperienceBase(BaseModel):
    experience_type: str
    title: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    position: Optional[str] = None
    role: Optional[str] = None
    desc: Optional[str] = None
    image: Optional[str] = None
    employer: Optional[str] = None
    employer_link: Optional[str] = None
    supervisor: Optional[str] = None
    supervisor_link: Optional[str] = None


class ExperienceCreate(ExperienceBase):
    user_id: int
    visible: bool = True


class Experience(ExperienceBase):
    experience_id: int

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    title: str
    sub_heading: Optional[str] = None
    thumb_img: Optional[str] = None
    tags: Optional[str] = None
    text: Optional[str] = None


class BlogCreate(BlogBase):
    user_id: int
    visible: bool = True


class Blog(BlogBase):
    blog_id: int

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
    user_id: int
    visible: bool = True


class Accolade(AccoladeBase):
    accolade_id: int

    class Config:
        orm_mode = True





