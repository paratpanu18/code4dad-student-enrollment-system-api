class Major:
    def __init__(self, major_name, academic_fees):
        self.__major_name = major_name
        self.__academic_fees = academic_fees
        self.__core_course_credit = 0
        self.__elective_course_credit = 0
        self.__core_course_list = []
        self.__elective_course_list = []
        

    @property
    def major_name(self):
        return self.__major_name
    
    @property
    def core_course_credit(self):
        return self.__core_course_credit
    @core_course_credit.setter
    def core_course_credit(self, new_course_credit):
        self.__core_course_credit += new_course_credit
        
    @property
    def elective_course_credit(self):
        return self.__elective_course_credit
    @elective_course_credit.setter
    def elective_course_credit(self, new_course_credit):
        self.__elective_course_credit += new_course_credit
    
    @property
    def core_course_list(self):
        return self.__core_course_list

    @property
    def elective_course_list(self):
        return self.__elective_course_list
    
    def add_core_course(self, course):
        self.core_course_credit += course.credit
        self.__core_course_list.append(course)

    def add_elective_course(self, course):
        self.elective_course_credit += course.credit
        self.__elective_course_list.append(course)
    
    def to_dict(self):
        return {
            "major_name": self.__major_name,
            "academic_fees": self.__academic_fees,
            "core_course_credit": self.__core_course_credit,
            "elective_course_credit": self.__elective_course_credit,
            "core_course_list": [course.course_id for course in self.__core_course_list],
            "elective_course_list": [course.course_id for course in self.__elective_course_list]
        }
        

    