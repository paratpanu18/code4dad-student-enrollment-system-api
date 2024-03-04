from Course import Course
from Teacher import Teacher

class Section():
    def __init__(self, course, section_number, teacher, max_student, location, schedule, semester, year):
        self.__course = course
        self.__section_number = section_number
        self.__teacher = teacher
        self.__max_student = max_student
        self.__location = location
        self.__schedule = schedule
        self.__semester = semester
        self.__year = year

        self.__student_list = []
        self.__wait_list = []
    
    @property
    def student_list(self):
        return self.__student_list
    
    @property
    def course(self):
        return self.__course

    @property
    def section_number(self):
        return self.__section_number
    
    @property
    def semester(self):
        return self.__semester
    
    @property
    def year(self):
        return self.__year
    
    def to_dict(self):
        return {
            "course": self.__course.course_name,
            "section_number": self.__section_number,
            "teacher": self.__teacher.name,
            "number_of_student": f'{len(self.__student_list)}/{self.__max_student}',
            "location": self.__location,
            "schedule": self.__schedule,
            "semester": self.__semester,
            "year": self.__year
        }

    def add_student_to_section(self, student):
        if len(self.__student_list) < self.__max_student:
            self.__student_list.append(student)
            return True
        else:
            self.__wait_list.append(student)
            return False
        
    def remove_student_from_section(self, student):
        if student in self.__student_list:
            self.__student_list.remove(student)
            if len(self.__wait_list) > 0:
                self.__student_list.append(self.__wait_list.pop(0))
            return True
        else:
            return False