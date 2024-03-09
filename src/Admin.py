from Account import Account

class Admin(Account):
    def __init__(self, admin_id, password, email, name, citizen_id):
        super().__init__(username = admin_id, 
                         password = password,
                         email = email,
                         name = name,
                         citizen_id = citizen_id, 
                         user_type = "admin")
        
        self.__admin_id = admin_id
    
    @property
    def admin_id(self):
        return self.__admin_id
    
    @property
    def name(self):
        return super().name
    
    
    def to_dict(self):
        return {
            "admin_id": self.__admin_id,
            "email": super().email,
            "name": super().name,
            "citizen_id": super().citizen_id
        }
