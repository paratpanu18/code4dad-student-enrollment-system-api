class Major():
    def __init__(self, name, academic_fees):
        self.__name = name
        self.__academic_fees = academic_fees
        self.__core_course_list = []
        self.__elective_course_list = []
        self.__elective_course_credit = 0
    
    def get_data(self):
        return {
            "major_name" : self.__name,
            "academic_fees" : self.__academic_fees,
            "core_course_list" : self.__core_course_list,
            "elective_course_list" : self.__elective_course_list,
            "elective_course_credit" : self.__elective_course_credit,
        }
        
    