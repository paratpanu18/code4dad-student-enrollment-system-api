class Course():
    def __init__(self, name, id, credit, course_type, grading_type: str = "Pass/Fail" or "Normal"):
        self.__name = name
        self.__credit = credit
        self.__course_type = course_type
        self.__grading_type = grading_type
        self.__id = id
        self.__section_list = []
        self.__pre_requisite_course_list = []
    
    def get_data(self):
        return {
            "course_id" : self.__id,
            "course_name" : self.__name,
            "credit" : self.__credit,
            "course_type" : self.__course_type,
            "grading_type" : self.__grading_type
        }
        