from University import kmitl

class Section():
    def __init__(self, section_id, course_id, teacher_id,
                  max_student, room, datetime, year , semester):
        self.__section_id = section_id
        self.__course = kmitl.get_course_by_course_id(course_id)
        self.__teacher = kmitl.get_teacher_by_teacher_id(teacher_id)
        self.__max_student = max_student
        self.__current_student = 0
        self.__datetime = datetime
        self.__room = room
        self.__year = year
        self.__semester = semester
        self.__student_list = []
        self.__co_requisite_section_list = []
        self.__enrollment_queue = []

    @property
    def course_id(self):
        return self.__course.course_id
    
    @property
    def section_id(self):
        return self.__section_id
    
    def set_co_requisite_section(self, section):
        self.__co_requisite_section_list.append(section)
    
    def add_student(self, student):
        self.__student_list.append(student)
        self.__current_student += 1
    
    def add_enrollment_queue(self, student):
        self.__enrollment_queue.append(student)

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