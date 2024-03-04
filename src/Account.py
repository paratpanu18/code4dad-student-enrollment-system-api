import datetime

from fastapi import HTTPException
from jose import jwt

from Util import email_is_valid, hash, settings

USER_TYPE_LIST = ["student", "teacher", "admin"]
JWT_SECRET = settings.JWT_SECRET
ALGORITHM = settings.ALGORITHM
TOKEN_EXPIRATION_TIME = 60 * 60         # 1 hour


class Account():
    def __init__(self, username, password, name, email, citizen_id, user_type):
        user_type = user_type.lower()
        if user_type not in USER_TYPE_LIST:
            raise HTTPException(status_code=400, detail="Invalid user type")
        
        if not email_is_valid(email):
            raise HTTPException(status_code=400, detail="Invalid email")

        self.__username = username
        self.__password = hash(password)
        self.__email = email
        self.__name = name
        self.__citizen_id = citizen_id
        self.__user_type = user_type

    @property
    def username(self):
        return self.__username

    @property
    def name(self):
        return self.__name
    
    @property
    def citizen_id(self):
        return self.__citizen_id
    
    @property
    def email(self):
        return self.__email
    
    def password_is_correct(self, password):
        return self.__password == hash(password)
    
    def create_token(self):
        expire_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKEN_EXPIRATION_TIME)
        to_encode = {
            "username": self.__username,
            "user_type": self.__user_type,
            "exp": expire_time
        }

        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)

        return encoded_jwt