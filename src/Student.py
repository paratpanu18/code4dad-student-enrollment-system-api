import datetime
from fastapi import APIRouter
from Account import Account

class Student(Account):
    type = "student"
    def __init__(self, name, citizen_id, email, password, 
                 student_id, major, faculty):
        super().__init__(name, citizen_id, email, password)
        
        self.__student_id = student_id 
        self.__major = major 
        self.__faculty = faculty 
        self.__year = datetime.datetime.now().year
        self.__transcript_list = []
        self.__is_graduated = False
    
    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def major(self):
        return self.__major
    
    @property
    def faculty(self):
        return self.__faculty
    
    @property
    def year(self):
        return self.__year
    
    @property
    def transcript_list(self):
        return self.__transcript_list
    
    def get_data(self):
        return {
            "student_id" : self.__student_id,
            "student_name" : super().name,
            "faculty" : self.__faculty,
            "year" : self.__year,
            "email" : super().email,
            "is_graduated" : self.__is_graduated
        }
    
    def enroll(self):
        pass
    
    def drop(self):
        pass
    
    def change_section(self):
        pass