class Account():
    def __init__(self, name, citizen_id, email, password):
        self.__name = name 
        self.__citizen_id = citizen_id 
        self.__email = email 
        self.__password = password 
        self.__is_graduated = False
