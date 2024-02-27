from Account import Account 
from Section import Section
from University import kmitl
from fastapi import APIRouter

teacher_router = APIRouter()
class Teacher(Account):
    type = "teacher"
    def __init__(self, name, citizen_id, email, password, teacher_id):
        super().__init__(name, citizen_id, email, password)
        self.__teacher_id = teacher_id
        self.__section_list = []
    
    @property
    def teacher_id(self):
        return self.__teacher_id

    def get_data(self):
        return {
            "teacher_id" : self.__teacher_id,
            "teacher_name" : super().name,
            "email" : super().email
        }
    
    def add_section(self, section: Section):
        course = kmitl.get_course_by_course_id(section.course_id)
        course.add_section(section)
    
    
    

