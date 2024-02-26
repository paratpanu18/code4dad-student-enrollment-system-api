from fastapi import APIRouter
from Schema import Student_Schema

university_router = APIRouter()
class University():
    def __init__(self, name):
        self.__name = name
        self.__faculty_list = []
        self.__student_list = []
        self.__teacher_list = []
        self.__admin_list = []
        self.__course_list = []
        
    def get_student_by_student_id(self, student_id):
        for student in self.__student_list:
            if student.student_id == student_id:
                return student
        return None
    
    def get_course_by_course_id(self, course_id):
        for course in self.__course_list:
            if course.id == course_id:
                return course
        return "course not found"
    
    def get_teacher_by_teacher_id(self, teacher_id):
        for teacher in self.__teacher_list:
            if teacher.teacher_id == teacher_id:
                return teacher
        return None
    
    def get_faculty_by_name(self, faculty_name):
        for faculty in self.__faculty_list:
            if faculty.faculty_name == faculty_name:
                return faculty
        return "faculty not found"
    
    def add_student(self, student):
        self.__student_list.append(student)

    def add_teacher(self, teacher):
        self.__teacher_list.append(teacher)

    def add_course(self, course):
        self.__course_list.append(course)
    

kmitl = University(name="KMITL")

@university_router.get("/get_user/{user_id}")
def get_user_data_by_user_id(user_id: str):
    student = kmitl.get_student_by_student_id(user_id)
    teacher = kmitl.get_teacher_by_teacher_id(user_id)
    if student:
        return student.get_data()
    if teacher:
        return teacher.get_data()
    
    return "User not found"

@university_router.get("/get_course/{course_id}")
def get_course_data_by_course_id(course_id: str):
    course = kmitl.get_course_by_course_id(course_id)
    if course:
        return course.get_data()
    return "Course not found"

@university_router.post("/add_student")
async def add_student(student: Student_Schema):
    kmitl.add_student(student)
    return student.get_data()
