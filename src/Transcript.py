from Enrollment import Enrollment

GRADE_MAPPING = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}

class Transcript():
    def __init__(self, semester, year):
        self.__semester = semester
        self.__year = year
        self.__enrollment_list = []
        self.__gps = None
        self.__gpa = None

    def add_enrollment(self, enrollment):
        self.__enrollment_list.append(enrollment)
        return enrollment.to_dict()

    def calculate_gps(self):
        total_credit = 0
        total_grade_point = 0
        for enrollment in self.__enrollment_list:
            course_grading_type = enrollment.section.course.grading_type
            if enrollment.grade != "N/A" and course_grading_type == "grade":
                total_credit += enrollment.credit
                total_grade_point += enrollment.credit * GRADE_MAPPING[enrollment.grade]
        self.__gps = total_grade_point / total_credit if total_credit > 0 else 0
        return self.__gps

    def to_dict(self):
        return {
            "semester": self.__semester,
            "year": self.__year,
            "enrollments": [enrollment.to_dict() for enrollment in self.__enrollment_list],
            "gps": self.__gps if self.__gps else "N/A"
        }