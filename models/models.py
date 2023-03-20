from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Boolean, sql, Date
from sqlalchemy.orm import relationship, validates, declarative_base
import re

Base = declarative_base()

class User(Base):
    '''
    DB model to store information about users
    '''
    __tablename__ = 'USER'
    full_name = Column(String(255))
    pronouns = Column(String(255))
    id = Column(Integer, primary_key=True, autoincrement=True, server_default=sql.func.rand())
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    
    verified = Column(Boolean, default=False)

    ###Images
    profile_img = Column(String(1000))
    thumb_img = Column(String(1000))
    cover_img = Column(String(1000))


    @staticmethod
    def is_valid_email(email):
        """
        Validates that an email address is in a valid format
        """
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        return bool(re.match(email_regex, email))

    @validates("email")
    def validate_email(self, key, email):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address")
        return email

class UserSecured(Base):
    '''
    Model to store user secrets
    '''
    __tablename__ = 'USER_SECURED'
    secured_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('USER.id'))
    email = Column(String(255))
    hashed_password = Column(String(255))
    disabled = Column(String(255))
    user_info = relationship(User)

class Contact(Base):
    '''
    Contact information of the users
    '''
    __tablename__ = "CONTACT"
    user_id = Column(Integer, ForeignKey('USER.id'))
    contact_id = Column(Integer, primary_key = True, server_default=sql.func.rand(),autoincrement=True)

    contact_value = Column(String(255),nullable=False)
    visible = Column(Boolean,nullable=False,default=True)
    contact_type = Column(Enum('SOCIAL_MEDIA','EMAIL','PHONE','PORTFOLIO'))
    thumb_img = Column(String(1000))
    thumb_txt = Column(String(255))

    user_info = relationship(User)

class Project(Base):
    '''
    All projects
    '''
    __tablename__ = "PROJECT"
    user_id = Column(Integer, ForeignKey("USER.id"))
    project_id = Column(Integer, primary_key = True, server_default=sql.func.rand(),autoincrement=True)
    project_type = Column(Enum('DEVELOPMENT','RESEARCH'), nullable=False)

    tags = Column(String(255))
    title = Column(String(255),nullable=False)
    sub_heading = Column(String(255))
    short_desc = Column(Text)
    long_desc = Column(Text)

    thumb_img = Column(String(1000))
    main_img = Column(String(1000))
    other_media = Column(String(1000))
    other_media_title = Column(String(255))

    code = Column(String(1000))
    paper = Column(String(1000))
    app = Column(String(1000))
    other_link = Column(String(1000))
    other_link_title = Column(String(255))

    user_info = relationship(User)

class Experience(Base):
    '''
    All experiences (work and study)
    '''
    __tablename__ = "EXPERIENCE"
    user_id = Column(Integer, ForeignKey("USER.id"))
    experience_id = Column(Integer, primary_key = True, server_default=sql.func.rand(),autoincrement=True)
    experience_type = Column(Enum('STUDY','INDUSTRY','ACADEMIC'), nullable=False)

    title = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    position = Column(String(255))
    role = Column(String(255))
    desc = Column(String(255))
    image = Column(String(1000))

    employer = Column(String(255))
    employer_link = Column(String(1000))
    supervisor = Column(String(255))
    supervisor_link = Column(String(1000))

    user_info = relationship(User)

class Blog(Base):
    '''
    Blog class
    '''
    __tablename__ = "BLOG"
    user_id = Column(Integer, ForeignKey("USER.id"))
    blog_id = Column(Integer, primary_key = True, server_default=sql.func.rand(),autoincrement=True)

    tilte = Column(String(255),nullable=False)
    sub_heading = Column(String(255))
    thumb_img = Column(String(1000))
    tags = Column(String(255))
    text = Column(Text)

    user_info = relationship(User)

class Accolade(Base):
    '''
    Achievements
    '''
    __tablename__ = "ACCOLADE"
    user_id = Column(Integer, ForeignKey("USER.id"))
    accolade_id = Column(Integer, primary_key = True, server_default=sql.func.rand(),autoincrement=True)

    title = Column(String(255),nullable=False)
    date = Column(Date)
    position = Column(String(255))
    role = Column(String(255))
    desc = Column(String(255))
    image = Column(String(1000))

    provider = Column(String(255))
    provider_link = Column(String(1000))

    user_info = relationship(User)