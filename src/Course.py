from fastapi import HTTPException

COURSE_TYPE = ["gened", "faculty", "curriculum"]
GRADING_TYPE = ["grade", "satisfactory"]

class Course():
    def __init__(self, 
                    course_id, 
                    course_name, 
                    credit, 
                    course_type: int,
                    grading_type: int):

        if COURSE_TYPE[course_type] is None:
            raise HTTPException(status_code=400, detail="Invalid course type. Course type must be one of the following: \
                                0 (gened), 1 (faculty), 2 (curriculum)")
        
        if GRADING_TYPE[grading_type] is None:
            raise HTTPException(status_code=400, detail="Invalid grading type. Grading type must be one of the following: \
                                0 (grade), 1 (satisfactory)")

        self.__course_id = course_id
        self.__course_name = course_name
        self.__credit = credit
        self.__course_type = COURSE_TYPE[course_type]
        self.__grading_type = GRADING_TYPE[grading_type]
        self.__section_list = []
        self.__pre_requisite_course_list = []

    @property
    def course_id(self):
        return self.__course_id
    
    @property
    def course_name(self):
        return self.__course_name
    
    @property
    def course_type(self):
        return self.__course_type
    
    @property
    def section_list(self):
        return self.__section_list
    
    @property
    def credit(self):
        return self.__credit

    @property
    def grading_type(self):
        return self.__grading_type
    
    def get_course_by_semester_year(self, semester, year):
        result = []
        for section in self.__section_list:
            if section.semester == semester and section.year == year:
                result.append(section)
        return result
        

    def to_dict(self):
        return {
            "course_id": self.__course_id,
            "course_name": self.__course_name,
            "credit": self.__credit,
            "course_type": self.__course_type,
            "grading_type": self.__grading_type
        }
    
    def get_section_by_section_number(self, section_number):
        for section in self.__section_list:
            if section.section_number == section_number:
                return section
        return None
    
    def add_section(self, new_section):
        for section in self.__section_list:
            if section.section_number == new_section.section_number and \
               section.semester == new_section.semester and \
               section.year == new_section.year:
                
                raise HTTPException(status_code=400, detail="Section already exists")


        self.__section_list.append(new_section)
        return new_section.to_dict()
    
    def __iter__(self):
        return iter(self.__section_list)
        