from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Boolean, sql
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
    profile_img = Column(String(1000))
    verified = Column(Boolean, default=False)

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

    user_info = relationship(User)

class Email(Base):
    '''
    Email addresses of the users
    '''
    __tablename__ = "EMAIL"
    user_id = Column(Integer, ForeignKey('USER.id'))


    user_info = relationship(User)

class Address(Base):
    '''
    Addresses of the users
    '''
    __tablename__ = "ADDRESS"
    user_id = Column(Integer, ForeignKey('USER.id'))

    user_info = relationship(User)

class Shop(Base):
    '''
    Each shop info (owned by a primary owner)
    '''
    __tablename__ = "SHOP"
    shop_id = Column(Integer, primary_key=True, server_default=sql.func.rand())
    primary_user_id = Column(Integer, ForeignKey('USER.id'))
    shop_name = Column(String(255))
    primary_user_info = relationship(User)

class ShopOwner(Base):
    '''
    A shop can have multiple owners and managers each with various roles
    '''
    __tablename__ = "SHOPOWNER"
    shop_id = Column(Integer, ForeignKey('SHOP.id'))
    user_id = Column(Integer, ForeignKey('USER.id'))
    access_level = Column(String(255),Enum("OWNER", "MANAGER", ""), nullable=False)
    shop_info = relationship(Shop)
    user_info = relationship(User)

class ShopToken(Base):
    '''
    Tokens associated against each external store for a given shop
    '''
    __tablename__ = "SHOP_TOKEN"
    token_id = Column(Integer, primary_key=True)
    shop_id = Column(Integer, ForeignKey('SHOP.id'))
    token = Column(String(255))
    store_type = Column(String(255), Enum("Facebook", "Amazon", "Flipkart"), nullable=False)
    shop_info = relationship(Shop)


class Product(Base):
    '''
    Product associated with each shop
    '''
    __tablename__ = "PRODUCT"
    product_id = Column(Integer, primary_key=True, server_default=sql.func.rand())
    shop_id = Column(Integer, ForeignKey('SHOP.id'))
    product_name = Column(String(255))
    count = Column(Integer(unsigned=False), nullable=False, default=0)
    shop_info = relationship(Shop)

