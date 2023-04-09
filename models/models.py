from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Boolean, sql, Date
from sqlalchemy.orm import relationship, validates, declarative_base
import uuid
from sqlalchemy.ext.hybrid import hybrid_property
import re
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

# class Template(Base):
#     '''
#     DB model to store template information
#     '''
#     __tablename__ = 'TEMPLATE'
#     _template_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)
#     location = Column(String(1000))
#     img = Column(String(1000))
#     title = Column(String(255))
#     desc = Column(String(255))


class User(Base):
    '''
    DB model to store information about users
    '''
    __tablename__ = 'USER'
    full_name = Column(String(255))
    pronouns = Column(String(255))
    _id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    bio = Column(String(1000))
    career_role = Column(String(255))

    summary = Column(String(1000))

    # _template_id = Column(UUID(as_uuid=True), ForeignKey('TEMPLATE._template_id'))
    
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
    _secured_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)
    _user_id = Column(UUID(as_uuid=True), ForeignKey('USER._id'))
    username = Column(String(255))
    hashed_password = Column(String(255))
    salt = Column(String(255))
    user_info = relationship(User)

class Contact(Base):
    '''
    Contact information of the users
    '''
    __tablename__ = "CONTACT"
    _user_id = Column(UUID(as_uuid=True), ForeignKey('USER._id'))
    _contact_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)

    contact_value = Column(String(255),nullable=False)
    visible = Column(Boolean,nullable=False,default=True)
    contact_type = Column(Enum('SOCIAL_MEDIA','EMAIL','PHONE','PORTFOLIO','GITHUB','LOCATION', name='contact_type'))
    thumb_img = Column(String(1000))
    thumb_txt = Column(String(255))

    user_info = relationship(User)

class Project(Base):
    '''
    All projects
    '''
    __tablename__ = "PROJECT"
    _user_id = Column(UUID(as_uuid=True), ForeignKey("USER._id"))
    _project_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)
    project_type = Column(Enum('DEVELOPMENT','RESEARCH','DESIGN',name='project_type'), nullable=False)

    tags = Column(String(255))
    title = Column(String(255),nullable=False)
    sub_heading = Column(String(255))
    short_desc = Column(Text)
    long_desc = Column(Text)
    visible = Column(Boolean, default=True, nullable=False)

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
    _user_id = Column(UUID(as_uuid=True), ForeignKey("USER._id"))
    _experience_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)
    experience_type = Column(Enum('STUDY','INDUSTRY','ACADEMIC',name='experience_type'), nullable=False)
    visible = Column(Boolean,nullable=False,default=True)

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
    _user_id = Column(UUID(as_uuid=True), ForeignKey("USER._id"))
    _blog_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)

    tilte = Column(String(255),nullable=False)
    sub_heading = Column(String(255))
    thumb_img = Column(String(1000))
    tags = Column(String(255))
    text = Column(Text)
    visible = Column(Boolean,nullable = False, default=True)

    user_info = relationship(User)

class Accolade(Base):
    '''
    Achievements
    '''
    __tablename__ = "ACCOLADE"
    _user_id = Column(UUID(as_uuid=True), ForeignKey("USER._id"))
    _accolade_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)

    title = Column(String(255),nullable=False)
    date = Column(Date)
    position = Column(String(255))
    role = Column(String(255))
    desc = Column(String(255))
    image = Column(String(1000))
    visible = Column(Boolean,nullable = False, default = True)

    provider = Column(String(255))
    provider_link = Column(String(1000))

    user_info = relationship(User)

class Skill(Base):
    '''
    List of skills for the user
    '''
    __tablename__ = "SKILLS"
    _user_id = Column(UUID(as_uuid=True), ForeignKey("USER._id"))
    _skill_id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, default=uuid.uuid4)

    skill_name = Column(String(255))

    user_info = relationship(User)
