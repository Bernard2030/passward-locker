#!/usr/bin/env python3.6
from unittest.main import main
from passward import User
from credentials import Credential


def create_new_user(user_name, email, password):
    '''
    create a new user with a username email and password
    '''
    new_user = User(user_name, email, password)
    return new_user

def save_user(user): 
    '''
     save a new user
    '''
    User.save_user()
def display_user():
    """
     display existing user
    """
    return User.display_user()
def login_user(user_name, email, password):
    """
     checks whether a user exist and then login the user in.
    """
  
    check_user = Credential.verify_user(user_name, email, password)
    return check_user

def create_new_credential(account,userName,password):
    """
    creates new credentials for a given user 
    """
    new_credential = Credential(account,userName,password)
    return new_credential
def save_credential(credentials):
    """
   save Credentials to the credentials list
    """
    Credential. save_details()
def display_accounts_details():
    """
     returns all the saved credential.
    """
    return Credential.display_credentials()

def delete_credential(credentials):
    """
    deletes a Credentials from credentials list
    """
    Credential.delete_credentials()

def find_credential(account):
    """
     finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credential.find_credential(account)
def check_credendtials(account):
    """
    checks if a Credentials exists with that account name and return true or false
    """
    return Credential.if_credential_exist(account)

def generatePassword():
    '''
    generates a random password for the user.
    '''
    auto_password=Credential.generatePassword()
    return auto_password


def passward_loccker():
    print("Welcome to passward-locker")
    print("\n Enter your short_code as follows.\n ca ---  Create New Account  \n li ---  Have an a/c  \n")
    short_code=input("").lower()
    if short_code == "ca":
        print("Get Account")
        print('*' * 50)
        user_name = input("User_name: ")
        while True:
            print(" ep - enter pasword:\n gp - generate random Password")
            password_Choice = input().lower()
            if password_Choice == 'ep':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generatePassword()
                break
            else:
                print("Invalid  try again")
        save_user(create_new_user(user_name,password))
        print("*"*85)
        print(f"Hello {user_name}, Your account has been created succesfully! Your password is: {password}")
        print("*"*80)
    elif short_code == "li":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        user_name = input("User name: ")
        password = input("password: ")
        login = login_user(user_name, password)
        if login_user == login:
            print(f"Hello {user_name}.Welcome to passWord-locker ")  
            print('\n')
    while True:
        print("Use these short codes:\n cc - Create a new credential \n dc - Display Credentials \n fc - Find a credential \n gp - Generate A randomn password \n d - Delete credential \n ex - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*50)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" ep - enter pasword if you already have an account:\n gp -  generate random Password")
                password_Choice = input().lower()
                if password_Choice == 'ep':
                    password = input("Enter Your  Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid passward try again")
            save_credential(create_new_credential(account,user_name, password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {user_name} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                 
                print('*' *50)
                print('*'*50)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{user_name}\n Password:{password}")
                    print('*'*50)
                print('*' *50)
            else:
                print("You don't have any credentials ..........")
        elif short_code == "fc":
            print("Enter the account name you're searching")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"account Name : {search_credential.account}")
                print('*' *50)
                print(f"user name: {search_credential.user_name} Password :{search_credential.password}")
                print('*' *50)
            else:
                print(" Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("*"*50)
                search_credential.delete_credential()
                print('\n')
                print(f"Your  credential for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print(" Credential you want to delete does not exist ")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords .. wlcome next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    passward_loccker()