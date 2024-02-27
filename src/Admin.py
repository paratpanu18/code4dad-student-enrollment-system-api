from Account import Account
from Student import Student
from Teacher import Teacher
from University import University
class Admin(Account):
    def __init__(self, name, citizen_id, email, password):
        super().__init__(name, citizen_id, email, password)
        
    def get_data(self):
        return {
            "admin_name" : self.__name,
            "email" : self.__email
        }



        