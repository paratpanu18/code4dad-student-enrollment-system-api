class Account():
    def __init__(self, name, citizen_id, email, password):
        self.__name = name 
        self.__citizen_id = citizen_id 
        self.__email = email 
        self.__password = password 

    @property
    def name(self):
        return self.__name
    
    @property
    def citizen_id(self):
        return self.__citizen_id
    
    @property
    def email(self):
        return self.__email
    
    