from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    name: str
    country: str
    email: EmailStr
    password: str
    phone: str