from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    full_name: Optional[str] = None
    pronouns: Optional[str] = None
    username: str
    email: str
    profile_img: Optional[str] = None
    verified: Optional[bool] = False


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    disabled: Optional[str] = None

    class Config:
        orm_mode = True


class UserSecuredBase(BaseModel):
    email: str
    hashed_password: str


class UserSecuredCreate(UserSecuredBase):
    user_id: int


class UserSecured(UserSecuredBase):
    secured_id: int
    user_id: int

    class Config:
        orm_mode = True


class ContactBase(BaseModel):
    user_id: int


class ContactCreate(ContactBase):
    contact_type: Optional[str] = None
    contact_value: Optional[str] = None


class Contact(ContactBase):
    id: int
    contact_type: Optional[str] = None
    contact_value: Optional[str] = None

    class Config:
        orm_mode = True


class EmailBase(BaseModel):
    user_id: int


class EmailCreate(EmailBase):
    email: str


class Email(EmailBase):
    id: int
    email: str

    class Config:
        orm_mode = True


class AddressBase(BaseModel):
    user_id: int


class AddressCreate(AddressBase):
    address_type: Optional[str] = None
    address_value: Optional[str] = None


class Address(AddressBase):
    id: int
    address_type: Optional[str] = None
    address_value: Optional[str] = None

    class Config:
        orm_mode = True


class ShopBase(BaseModel):
    primary_user_id: int
    shop_name: str


class ShopCreate(ShopBase):
    pass


class Shop(ShopBase):
    shop_id: int

    class Config:
        orm_mode = True


class ShopOwnerBase(BaseModel):
    shop_id: int
    user_id: int
    access_level: str


class ShopOwnerCreate(ShopOwnerBase):
    pass


class ShopOwner(ShopOwnerBase):
    id: int

    class Config:
        orm_mode = True


class ShopTokenBase(BaseModel):
    shop_id: int
    token: str
    store_type: str


class ShopTokenCreate(ShopTokenBase):
    pass


class ShopToken(ShopTokenBase):
    token_id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    shop_id: int
    product_name: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int
    count: int

    class Config:
        orm_mode = True
