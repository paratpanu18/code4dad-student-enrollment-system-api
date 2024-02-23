from Course import Course
from Teacher import Teacher
class Section():
    def __init__(self, section_id, course : Course, teacher : Teacher,
                  max_student, current_student, room, datetime, year , semester):
        self.__section_id = section_id
        self.__course = course
        self.__teacher = teacher
        self.__max_student = max_student
        self.__current_student = current_student
        self.__datetime = datetime
        self.__room = room
        self.__year = year
        self.__semester = semester
        self.__student_list = []
        self.__co_requisite_section_list = []
        self.__enrollment_queue = []
 
    def get_data(self):
        return {
            "section_id" : self.__section_id,
            "course" : self.__course.get_data(),
            "teacher" : self.__teacher.get_data(),
            "max_student" : self.__max_student,
            "current_student" : self.__current_student,
            "room" : self.__room,
            "datetime" : self.__datetime,
            "year" : self.__year,
            "semester" : self.__semester
        }