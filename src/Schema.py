from pydantic import BaseModel

class LoginCredentials(BaseModel):
    username: str
    password: str

class InsertStudent(BaseModel):
    student_id: str
    password: str
    email: str
    name: str
    citizen_id: str
    major: str
    faculty: str

class InsertTeacher(BaseModel):
    teacher_id: str
    password: str
    email: str
    name: str
    citizen_id: str

class InsertCourse(BaseModel):
    course_name: str
    course_id: str
    credit: int
    course_type: int
    grading_type: int

class InsertSection(BaseModel):
    course_id: str
    section_number: int
    teacher_id: str
    max_student: int
    location: str
    schedule: str
    semester: str
    year: int

class Enroll(BaseModel):
    student_id: str
    course_id: str
    section_number: int
