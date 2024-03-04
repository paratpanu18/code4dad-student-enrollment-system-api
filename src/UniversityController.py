from fastapi import APIRouter, HTTPException, Depends

from Student import Student
from Teacher import Teacher
from Course import Course
from Section import Section
from Util import get_current_user
import Schema

university_router = APIRouter(tags=["university"])
authenticator_router = APIRouter(tags=["authenticator"])
student_router = APIRouter(tags=["student"])
teacher_router = APIRouter(tags=["teacher"])
course_router = APIRouter(tags=["course and section"])

class University():
    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__faculty_list = []
        self.__course_list = []

    def get_student_by_student_id(self, student_id):
        for user in self.__user_list:
            if isinstance(user, Student) and user.student_id == student_id:
                return user
        return None
    
    def get_student_data_by_student_id(self, student_id):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student.to_dict()

    def login(self, username, password):
        for user in self.__user_list:
            if user.username == username and user.password_is_correct(password):
                return user.create_token()
        raise HTTPException(status_code=404, detail="Login credentials are incorrect")

    def add_student(self, student_id, password, email, name, citizen_id, major, faculty):
        if self.get_student_by_student_id(student_id) is not None:
            raise HTTPException(status_code=400, detail="Student ID already exists")

        new_student = Student(student_id, password, email, name, citizen_id, major, faculty)
        self.__user_list.append(new_student)
        return new_student.to_dict()
    
    def enroll_student_to_section(self, student_id, course_id, section_number):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        # Check if student is already enrolled in the course
        for section in course.section_list:
            if student in section.student_list:
                raise HTTPException(status_code=400, detail="Student already enrolled in course")

        section = course.get_section_by_section_number(section_number)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        if section.add_student_to_section(student):
            return student.enroll_to_section(section)
        
        raise HTTPException(status_code=400, detail="Failed to enroll student to section. Section is full.")
    
    def drop_student_from_section(self, student_id, course_id, section_number):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number(section_number)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        if student not in section.student_list:
            raise HTTPException(status_code=400, detail="Student is not enrolled in section")
        
        # Section.drop_student_from_section() returns False if there is no student in the wait list
        # Otherwise, it returns student object
        next_student_in_wait_list = section.drop_student_from_section(student)
        student.drop_from_section(section)

        if next_student_in_wait_list is not False:
            # In case there is a student in the wait list, enroll the student to the section
            self.enroll_student_to_section(next_student_in_wait_list.student_id, course_id, section_number)

        return student.to_dict()

    def get_student_enrolled_courses(self, student_id, semester, year):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        transcript = student.get_transcript_by_semester_and_year(semester, year)

        if transcript is not None:
            return transcript.get_enrollment_list()
        
        raise HTTPException(status_code=404, detail="Transcript not found")

    def get_teacher_by_teacher_id(self, teacher_id):
        for user in self.__user_list:
            if isinstance(user, Teacher) and user.teacher_id == teacher_id:
                return user
        return None
    
    def get_teacher_data_by_teacher_id(self, teacher_id):
        teacher = self.get_teacher_by_teacher_id(teacher_id)
        if teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return teacher.to_dict()

    def add_teacher(self, teacher_id, password, email, name, citizen_id):
        if self.get_teacher_by_teacher_id(teacher_id) is not None:
            raise HTTPException(status_code=400, detail="Teacher ID already exists")
        
        new_teacher = Teacher(teacher_id, password, email, name, citizen_id)
        self.__user_list.append(new_teacher)
        return new_teacher.to_dict()
    
    def add_course(self, course_name, course_id, credit, course_type, grading_type):
        if self.get_course_by_course_id(course_id) is not None:
            raise HTTPException(status_code=400, detail="Course ID already exists")

        new_course = Course(course_id, course_name, credit, course_type, grading_type)
        self.__course_list.append(new_course)
        return new_course.to_dict()
    
    def add_section(self, course_id, section_number, teacher_id, max_student, location, schedule, semester, year):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        teacher = self.get_teacher_by_teacher_id(teacher_id)
        if teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        new_section = Section(course, section_number, teacher, max_student, location, schedule, semester, year)
        course.add_section(new_section)

        teacher.add_taught_section(new_section)

        return new_section.to_dict()
    
    def get_course_by_course_id(self, course_id):
        for course in self.__course_list:
            if course.course_id == course_id:
                return course
        return None
    
    def get_course_data_by_course_id(self, course_id):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        return course.to_dict()
    
    def get_all_sections_data_by_course_id(self, course_id):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        return [section.to_dict() for section in course]

kmitl = University(name="KMITL")


# Student
@student_router.post("/add_student")
async def add_student(student: Schema.InsertStudent):
    return kmitl.add_student(student.student_id, 
                             student.password, 
                             student.email, 
                             student.name, 
                             student.citizen_id, 
                             student.major, 
                             student.faculty)

@student_router.get("/get_student_by_student_id/{student_id}")
async def get_student_by_student_id(student_id: str):
    return kmitl.get_student_data_by_student_id(student_id)

@student_router.post("/enroll")
async def enroll(enroll: Schema.Enroll):
    return kmitl.enroll_student_to_section(enroll.student_id, enroll.course_id, enroll.section_number)

@student_router.post("/drop")
async def drop(drop: Schema.Enroll):
    return kmitl.drop_student_from_section(drop.student_id, drop.course_id, drop.section_number)

@student_router.get("/get_student_enrolled_courses/{student_id}/{semester}/{year}")
async def get_student_enrolled_courses(student_id: str, semester: int, year: int):
    return kmitl.get_student_enrolled_courses(student_id, semester, year)

# Teacher
@teacher_router.post("/add_teacher")
async def add_teacher(teacher: Schema.InsertTeacher):
    return kmitl.add_teacher(teacher_id=teacher.teacher_id,
                            password=teacher.password,
                            email=teacher.email,
                            name=teacher.name,
                            citizen_id=teacher.citizen_id)

@teacher_router.get("/get_teacher_by_teacher_id/{teacher_id}")
async def get_teacher_by_teacher_id(teacher_id: str):
    return kmitl.get_teacher_data_by_teacher_id(teacher_id)

# Course
@course_router.get("/get_course_by_course_id/{course_id}")
async def get_course_by_course_id(course_id: str):
    return kmitl.get_course_data_by_course_id(course_id)

@course_router.post("/add_course")
async def add_course(course: Schema.InsertCourse):
    return kmitl.add_course(course.course_name, 
                            course.course_id, 
                            course.credit, 
                            course.course_type, 
                            course.grading_type)

@course_router.post("/add_section")
async def add_section(section: Schema.InsertSection):
    return kmitl.add_section(section.course_id, 
                            section.section_number, 
                            section.teacher_id, 
                            section.max_student,
                            section.location, 
                            section.schedule, 
                            section.semester, 
                            section.year)

@course_router.get("/get_all_sections_by_course_id/{course_id}")
async def get_all_sections_by_course_id(course_id: str):
    return kmitl.get_all_sections_data_by_course_id(course_id)

# Authenticator
@authenticator_router.post("/login")
async def login(credentials: Schema.LoginCredentials):
    return kmitl.login(credentials.username, credentials.password)

