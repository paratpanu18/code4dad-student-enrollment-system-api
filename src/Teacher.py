from Account import Account

class Teacher(Account):
    def __init__(self, teacher_id, password, email, name, citizen_id):
        super().__init__(username = teacher_id, 
                         password = password,
                         email = email,
                         name = name,
                         citizen_id = citizen_id, 
                         user_type = "teacher")
        
        self.__teacher_id = teacher_id
        self.__section_taught = []
    
    @property
    def teacher_id(self):
        return self.__teacher_id
    
    @property
    def name(self):
        return super().name
    
    @property
    def section_taught(self):
        return self.__section_taught
    
    def add_taught_section(self, section):
        self.__section_taught.append(section)

    def get_all_sections_taught_by_semester_and_year(self, semester, year):
        sections = []
        for section in self.__section_taught:
            if section.semester == semester and section.year == year:
                sections.append(section.to_dict())
        return sections
        


    
    def to_dict(self):
        return {
            "teacher_id": self.__teacher_id,
            "email": super().email,
            "name": super().name,
            "citizen_id": super().citizen_id
        }