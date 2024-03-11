from Course import Course
from Teacher import Teacher
from Student import Student

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
        self.__co_requisite_section = None
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
    
    @property
    def schedule(self): 
        return self.__schedule
    
    @property
    def location(self):
        return self.__location
    
    @property
    def wait_list(self):
        return self.__wait_list
    
    @property
    def max_student(self):
        return self.__max_student
    
    @property
    def co_requisite_section(self):
        return self.__co_requisite_section
    
    def to_dict(self):
        return {
            "course_id": self.__course.course_id,
            "course_name": self.__course.course_name,
            "section_number": self.__section_number,
            "grading_type": self.__course.grading_type,
            "teacher": self.__teacher.name,
            "number_of_student": f'{len(self.__student_list)}/{self.__max_student}',
            "location": self.__location,
            "schedule": self.__schedule,
            "semester": self.__semester,
            "year": self.__year
        }
    
    def get_next_student_in_wait_list(self):
        return self.__wait_list.pop(0) if len(self.__wait_list) > 0 else None

    def add_student_to_section(self, student):
        if len(self.__student_list) < self.__max_student:
            self.__student_list.append(student)
            return True
        else:
            self.__wait_list.append(student)
            return False
        
    def drop_student_from_section(self, student):
        if student in self.__student_list:
            self.__student_list.remove(student)
            if len(self.__wait_list) > 0:
                return self.__student_list.pop(0)
            else:
                return False
            
    def get_grade_and_score_student(self):
        result = []
        for student in self.__student_list:
            result.append(student.get_grade_and_score_by_section(self))
        return result
    
    def add_co_requisite_section(self, co_requisite_section):
        self.__co_requisite_section = co_requisite_section
        return co_requisite_section.to_dict()
    
    def get_co_requisite_section(self):
        return [section.to_dict() for section in self.__co_requisite_section_list]