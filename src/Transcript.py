from fastapi import HTTPException

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

    @property
    def semester(self):
        return self.__semester
    
    @property
    def year(self):
        return self.__year

    @property
    def enrollment_list(self):
        return self.__enrollment_list

    def add_enrollment(self, student, section):
        new_enrollment = Enrollment(student, section)
        self.__enrollment_list.append(new_enrollment)
        return new_enrollment.to_dict()
    
    def drop_enrollment(self, section):
        for enrollment in self.__enrollment_list:
            if enrollment.section == section and enrollment.grade == "N/A":
                self.__enrollment_list.remove(enrollment)
                self.calculate_gps()
                return True
        raise HTTPException(status_code=400, detail="Student is not enrolled in the section or the grade is already given")


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
            "enrollments": [enrollment.to_dict_with_grade() for enrollment in self.__enrollment_list],
            "gps": self.__gps if self.__gps else "N/A"
        }
    
    def get_enrollment_list(self):
        result = []
        for enrollment in self.__enrollment_list:
            result.append(enrollment.to_dict())

        return result
    
    def add_grade(self, section, grade):
        for enrollment in self.__enrollment_list:
            if enrollment.section == section:
                enrollment.grade = grade
                self.calculate_gps()
                return enrollment.to_dict()
        raise ValueError("Student is not enrolled in the section")
    
    def get_enrollment_by_section(self, section):
        for enrollment in self.__enrollment_list:
            if enrollment.section == section:
                return enrollment
        return None