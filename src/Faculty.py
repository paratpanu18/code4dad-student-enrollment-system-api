class Faculty():
    def __init__(self, name):
        self.__name = name
        self.__major_list = []
    
    def get_data(self):
        return {
            "faculty_name" : self.__name,
            "major_list" : self.__major_list
        }