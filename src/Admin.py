from Account import Account

class Admin(Account):
    def __init__(self, name, citizen_id, email, password):
        super().__init__(name, citizen_id, email, password)
        
    def get_data(self):
        pass
    
        