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
    @grade.setter
    def grade(self, grade):
        if grade not in ["A", "B+", "B", "C+", "C", "D+", "D", "F", "N/A"]:
            raise ValueError("Invalid grade. Grade must be one of the following: A, B+, B, C+, C, D+, D, F")
        self.__grade = grade
    
    def to_dict(self):
        return {
            "course_id": self.__section.course.course_id,
            "course_name": self.__section.course.course_name,
            "credit": self.__section.course.credit,
            "section_number": self.__section.section_number,
            "schedule": self.__section.schedule,
            "location": self.__section.location,
        }

    def to_dict_with_grade(self):
        return {
            "course_id": self.__section.course.course_id,
            "course_name": self.__section.course.course_name,
            "credit": self.__section.course.credit,
            "section_number": self.__section.section_number,
            "grade": self.__grade if self.__grade else "N/A"
        }