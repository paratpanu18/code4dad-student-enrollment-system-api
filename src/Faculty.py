from Major import Major

class Faculty:
    def __init__(self, faculty_name):
        self.__faculty_name = faculty_name
        self.__major_list = []

    @property
    def faculty_name(self):
        return self.__faculty_name
    
    @property
    def majors_list(self):
        return self.__major_list
    
    def get_major_by_major_name(self, major_name):
        for major in self.__major_list:
            if major.major_name == major_name:
                return major
        return None
    
    def add_major(self, major):
        self.__major_list.append(major)
    
    def to_dict(self):
        return {
            "faculty_name": self.__faculty_name,
            "major_list": [major.major_name for major in self.__major_list]
        }