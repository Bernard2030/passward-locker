import random
import string


class Credential:
    """
    A class that generates new user credentials
    """
    pass
credential_list = []

def __init__(self, account, user_name, email, passward):
    self.account = account
    self.user_name = user_name
    self.email = email
    self.passward = passward
    

def save_credential(self):
    """
    save_credential method saves credential objects into credential_list
    """
    Credential.credential_list.append()

def delete_credential(self):
    """
    delete_credential function that delete an accountncredential from credential_list
    """

    Credential.credential_list.remove(self)    

@classmethod
def display_credential(cls):
    """
    method that returns the credential_list
    """        

    return cls.credential_list

@classmethod
def find_credential(cls, account):
    """
    Method that takes in account_name returns credential martching the account name 
    """

    for credential in cls.credential_list:
        if credential.account == account:
            return credential

@classmethod
def  credential_exist(cls,account):
    """
    Method to check if credential exist from credential_list
    """
    for credential in cls.credential_list:
        if credential.account == account:
            return True
        return False   

def generatePassward(stringlength=9):
    """
    Generating a random passward of string,letters and digits and unique characters
    """
    passward = string.ascii_uppercase + string.ascii_lowercase + string.digits 
    + "#%$^&*!"
    return "".join(random.choice(passward) for i in range (stringlength))                   

    