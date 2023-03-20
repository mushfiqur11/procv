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
    contact_value = Column()

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