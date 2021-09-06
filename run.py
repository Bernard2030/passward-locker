#!/usr/bin/env python3.6
from unittest.main import main
from passward import User
from credentials import Credential


def create_new_user(user_name, email, password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(user_name, email, password)
    return new_user

def save_user(user): 
    '''
    Function to save a new user
    '''
    User.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(user_name, email, password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credential.verify_user(user_name, email, password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credential(account,userName,password)
    return new_credential
def save_credential(credentials):
    """
    Function to save Credentials to the credentials list
    """
    Credential. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credential.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    Credential.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credential.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credential.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credential.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credential.copy_password(account)


def pmain():
    print("Welcome to passward-locker")
    print("\n Enter your short_code as follows.\n ca ---  Create New Account  \n li ---  Have an a/c  \n")
    short_code=input("").lower()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        user_name = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(user_name,password))
        print("*"*85)
        print(f"Hello {user_name}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        user_name = input("User name: ")
        password = input("password: ")
        login = login_user(user_name,password)
        if login_user == login:
            print(f"Hello {user_name}.Welcome To PassWord Locker Manager")  
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credential(create_new_credential(account,user_name,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {user_name} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{user_name}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.user_name} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    pmain()