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
    semester: int
    year: int

class Enroll(BaseModel):
    student_id: str
    course_id: str
    section_number: int

class InsertFaculty(BaseModel):
    faculty_name: str

class InsertMajor(BaseModel):
    faculty_name: str
    major_name: str
    academic_fees: int

class InsertCourseToMajor(BaseModel):
    faculty_name: str
    major_name: str
    course_id: str
    course_group: str

class ChangeSection(BaseModel):
    student_id: str
    course_id: str
    old_section_number: int
    new_section_number: int

class GradeAssignment(BaseModel):
    student_id: str
    course_id: str
    section_number: int
    grade: str

class InsertPreRequisite(BaseModel):
    course_id: str
    pre_requisite_course_id: str
