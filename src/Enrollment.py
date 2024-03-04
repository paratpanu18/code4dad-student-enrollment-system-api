class Enrollment():
    def __init__(self, student, section):
        self.__student = student
        self.__section = section
        self.__grade = None

    @property
    def course_name(self):
        return self.__section.course.course_name
    
    @property
    def credit(self):
        return self.__section.course.credit
    
    @property
    def section(self):
        return self.__section
    
    @property
    def grade(self):
        return self.__grade if self.__grade else "N/A"
    
    def to_dict(self):
        return {
            "course": self.__section.course.course_name,
            "credit": self.__section.course.credit,
            "section_number": self.__section.section_number,
            "grade": self.__grade if self.__grade else "N/A"
        }