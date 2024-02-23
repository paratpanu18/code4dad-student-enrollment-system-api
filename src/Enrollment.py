from Grade import Grade
class Enrollment():
    def __init__(self, student, course, semester, year, datetime, grade: Grade):
        self.__student = student
        self.__course = course
        self.__semester = semester
        self.__year = year
        self.__datetime = datetime
        self.__grade = grade
        
