from pydantic import BaseModel

class Student_Schema(BaseModel):
    name: str
    citizen_id: str
    email: str
    password: str
    student_id: str
    major: str
    faculty: str
