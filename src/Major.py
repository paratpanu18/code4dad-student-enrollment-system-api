class Major:
    def __init__(self, major_name, academic_fees, elective_course_credit):
        self.__major_name = major_name
        self.__academic_fees = academic_fees
        self.__elective_course_credit = elective_course_credit
        self.__core_course_list = []
        self.__elective_course_list = []

    @property
    def major_name(self):
        return self.__major_name
    
    @property
    def elective_course_credit(self):
        return self.__elective_course_credit
    
    @property
    def core_course_list(self):
        return self.__core_course_list
    
    @property
    def elective_course_list(self):
        return self.__elective_course_list
    
    def to_dict(self):
        return {
            "major_name": self.__major_name,
            "academic_fees": self.__academic_fees,
            "elective_course_credit": self.__elective_course_credit,
            "core_course_list": [course.course_id for course in self.__core_course_list],
            "elective_course_list": [course.course_id for course in self.__elective_course_list]
        }
        

    