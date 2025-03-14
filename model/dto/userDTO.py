# model/dto/userDTO.py
class UserDTO:
    def __init__(self):
        self.id = None
        self.email = None
        self.role = None
        self.exp = None
        self.session = None
    
    def is_Empty(self):
        return self.id == None and self.email == None and self.role == None and self.exp == None and self.session == None

    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id

    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email

    def get_role(self):
        return self.role
    def set_role(self, role):
        self.role = role

    def get_exp(self):
        return self.exp
    def set_exp(self, exp):
        self.exp = exp

    def get_session(self):
        return self.session
    def set_session(self, session):
        self.session = session
    
    def user_to_json(self):
        # To Be Complete
        pass
