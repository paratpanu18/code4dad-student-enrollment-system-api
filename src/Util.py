import re
import hashlib
import datetime

from pydantic_settings import BaseSettings
from jose import JWTError, jwt
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class Settings(BaseSettings):
    # JWT Token
    JWT_SECRET: str
    ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

def email_is_valid(email):
    # Regular expression for email validation
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
    
def hash(password):
    # Hash the password using SHA256
    return hashlib.sha256(password.encode()).hexdigest()

def verify_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        if payload.get("type") not in ["student", "admin", "teacher"] or payload.get("exp") is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        else:
            return payload.get("username")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
def get_current_user(token: str = Depends(oauth2_scheme)):

    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    username = verify_token(token, credential_exception)
    if username:
        return username
    raise credential_exception

def get_current_semester():
    # Get the current semester and year
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    semester_1 = [6, 7, 8, 9, 10]
    semester_2 = [11, 12, 1, 2, 3]

    if current_month in semester_1:
        return 1
    elif current_month in semester_2:
        return 2
    else:
        return 3 # For summer semester

def get_current_academic_year():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    SEMESTER_2 = 2
    SUMMER = 3

    if get_current_semester() == SEMESTER_2 and current_month in [1, 2, 3]:
        return current_year - 1
    elif get_current_semester() == SUMMER:
        return current_year - 1
    else:
        return current_year