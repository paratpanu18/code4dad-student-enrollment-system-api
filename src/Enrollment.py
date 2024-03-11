from Grade import Grade

class Enrollment():
    def __init__(self, student, section):
        self.__student = student
        self.__section = section
        self.__grade = None
        self.__score = {
            "score_1": 0,
            "score_2": 0,
            "score_3": 0,
            "score_4": 0
        }

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
    def score(self):
        return self.__score
    
    
    @property
    def grade(self):
        return self.__grade if self.__grade else "N/A"
    @grade.setter
    def grade(self, grade):
        course_type = self.__section.course.course_type
        if course_type is "grade" and grade not in ["A", "B+", "B", "C+", "C", "D+", "D", "F", "N/A"]:
            raise ValueError("Invalid grade. Grade must be one of the following: A, B+, B, C+, C, D+, D, F")
        elif course_type is "satisfactory" and grade not in ["S", "U", "N/A"]:
            raise ValueError("Invalid grade. Grade must be one of the following: S, U")
        self.__grade = grade

    def to_dict(self):
        return {
            "course_id": self.__section.course.course_id,
            "course_name": self.__section.course.course_name,
            "credit": self.__section.course.credit,
            "section_number": self.__section.section_number,
            "semester": self.__section.semester,
            "year": self.__section.year,
            "schedule": self.__section.schedule,
            "location": self.__section.location,
            "grade": self.__grade if self.__grade else "N/A",
            "score": self.__score
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
            "score": self.__score
        }