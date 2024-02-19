from Account import Account

class Student(Account):
    def __init__(self, name, citizen_id, email, password, is_graduated: bool,
                 student_id, major, faculty, year):
        super().__init__(name, citizen_id, email, password, is_graduated)
        
        self.__student_id = student_id 
        self.__major = major 
        self.__faculty = faculty 
        self.__year = year
        self.__transcript_list = []
    
    def get_data(self):
        return {
            "student_id" : self.__student_id,
            "student_name" : self.__name,
            "faculty" : self.__faculty,
            "year" : self.__year,
            "email" : self.__email,
            "is_graduated" : self.__is_graduated
        }
    
    def enroll(self):
        pass
    
    def drop(self):
        pass
    
    def change_section(self):
        pass
    
        