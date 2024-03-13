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
    
def time_is_intersect(time_range1, time_range2):
    # Parse time ranges
    day1, time_range1 = time_range1.split(' ', 1)
    day2, time_range2 = time_range2.split(' ', 1)

    start_time1, end_time1 = time_range1.split(' - ')
    start_time2, end_time2 = time_range2.split(' - ')

    # Convert time strings to datetime objects
    start_datetime1 = datetime.datetime.strptime(day1 + ' ' + start_time1, '%a %H:%M')
    end_datetime1 = datetime.datetime.strptime(day1 + ' ' + end_time1, '%a %H:%M')
    start_datetime2 = datetime.datetime.strptime(day2 + ' ' + start_time2, '%a %H:%M')
    end_datetime2 = datetime.datetime.strptime(day2 + ' ' + end_time2, '%a %H:%M')

    # Check for intersection
    if day1 == day2 and (start_datetime1 <= end_datetime2 and end_datetime1 >= start_datetime2):
        return True
    else:
        return False

def grade_and_score_format_is_correct(grade_and_score_dict: dict):
    for student_id, grade_and_score in grade_and_score_dict.items():
        grade = grade_and_score["grade"]
        if grade not in ["A", "B+", "B", "C+", "C", "D+", "D", "F", "S", "U", "N/A"]:
            return False
        
        for score_name, score in grade_and_score["score"].items():
            if score_name not in ["score_1", "score_2", "score_3", "score_4"]:
                return False
            if score < 0 or not (isinstance(score, int) or isinstance(score, float)):
                return False
            
    return True
