from Grade import Grade

class Enrollment():
    def __init__(self, student, section):
        self.__student = student
        self.__section = section
        self.__grade = None
        self.__score_1 = None
        self.__score_2 = None
        self.__score_3 = None
        self.__score_4 = None

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

    @property
    def score_1(self):
        return self.__score_1 if self.__score_1 else "N/A"
    @score_1.setter
    def score_1(self, score_1):
        self.__score_1 = score_1

    @property
    def score_2(self):
        return self.__score_2 if self.__score_2 else "N/A"
    @score_2.setter
    def score_2(self, score_2):
        self.__score_2 = score_2

    @property
    def score_3(self):
        return self.__score_3 if self.__score_3 else "N/A"
    @score_3.setter
    def score_3(self, score_3):
        self.__score_3 = score_3

    @property
    def score_4(self):
        return self.__score_4 if self.__score_4 else "N/A"
    @score_4.setter
    def score_4(self, score_4):
        self.__score_4 = score_4

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
    
    def to_dict_with_student(self):
        return {
            "student_id": self.__student.student_id,
            "email": self.__student.email,
            "name": self.__student.name,
            "citizen_id": self.__student.citizen_id,
            "major": self.__student.major,
            "faculty": self.__student.faculty,
            "year_entered": self.__student.year_entered,
            "course_id": self.__section.course.course_id,
            "grade": self.__grade if self.__grade else "N/A",
            "score_1": self.__score_1 if self.__score_1 else "N/A",
            "score_2": self.__score_2 if self.__score_2 else "N/A",
            "score_3": self.__score_3 if self.__score_3 else "N/A",
            "score_4": self.__score_4 if self.__score_4 else "N/A"
        }