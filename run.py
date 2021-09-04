from passward import User
from credentials import Credential
import random

def create_user(username, passward, email):
    """
    Function creating new user
    """

    new_user = User(username, passward, email)
    return new_user

def save_user(user):
    """
    Function to save a new user
    """    
    user.save_user()
     
def display_user():
    """
    function to display created or existing user
    """     
    return User.display_user()

def sign_in_user(user_name, passward,email):
    """
    Function to log in in existing user account if the user has an account
    """    

    log_user = Credential.verify_user(user_name, passward, email)

    return log_user

def create_new_credential(user_name, passward, email):
    """
    Function to create new credential for a given user name
    """
    new_credential = Credential(user_name, passward, email)
    return new_credential

def save_credential(credential):
    """
    A function to save new created credential to the credential list
    """ 
    credential.save_user()

def delete_credential(credential):
    """
    Function to delete credential from the credential_list
    """    
    credential.delete_credential()

def search_credential(user_name):
    """
    Function to look for credential and return credential that belongs to the user_name
    """ 
    return Credential.search_credential(user_name) 

def display_credential():
    """
    Function that will return saved credentials for the user
    """    
    return Credential.display_credential()

def generate_passward():
    """
    Function to generate random passward for the user.
    """    
    auto_passward = Credential.generatePassward()
    return auto_passward

def cop_passward(user_name):
    """
    A function that copies passward using the pyperclip framework
    """    
    return Credential.copy_passward(user_name)






