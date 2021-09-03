class Credential:
    """
    A class that generates new user credentials
    """
    pass
credentials_list = []

def __init__(self, user_name, passward, email):
    self.user_name = user_name
    self.passward = passward
    self.email = email

def save_credential(self):
    """
    save_credential method saves credential objects into credential_list
    """
    Credentials.credential_list.append(self)

@classmethod
def display_credential(cls):
    """
    method that returns the credential_list
    """        

    return cls.credentials_list