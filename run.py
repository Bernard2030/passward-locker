#!/usr/bin/env python3.6
from passward import User
from credentials import Credential
import random
import string

def create_user(username, passward, email):# create anew user
    """
    Function creating new user
    """

    new_user = User(username, passward, email)
    return new_user

def save_user(user):#save user
    """
    Function to save a new user
    """    
    user.save_user()
     
def display_user():#display user
    """
    function to display created or existing user
    """     
    return User.display_user()

def sign_in_user(user_name, passward,email):#check if user exist
    """
    Function to log in in existing user account if the user has an account
    """    

    log_user = Credential.verify_user(user_name, passward, email)

    return log_user

def check_existing_user(user_name):
    """
    check if user exists
    """
    return User.user_exist(user_name)


#  create new credential
def create_new_credential(user_name, passward, email):
    """
    Function to create new credential for a given user name
    """
    new_credential = Credential(user_name, passward, email)
    return new_credential

def save_credential(credential):  #save credential
    """
    A function to save new created credential to the credential list
    """ 
    credential.save_user()

def delete_credential(credential): # delete credential
    """
    Function to delete credential from the credential_list
    """    
    credential.delete_credential()

def find_credential(user_name): #find credential
    """
    Function to look for credential and return credential that belongs to the user_name
    """ 
    return Credential.search_credential(user_name) 

def display_credential(): #display credential
    """
    Function that will return saved credentials for the user
    """    
    return Credential.display_credential()

def generate_passward(): # generate passward
    """
    Function to generate random passward for the user.
    """    
    auto_passward = Credential.generatePassward()
    return auto_passward

def    passward_locker():# main function
   
        print("Welcome to passward locker!!")

while True:
        print('*' *50)
       
        print("Select a short code to  continue:... \n ca - create a/c, \n lg - login to a/c, \n da- display a/c, \n ex - exit from the application ")
        print('*' *50)
        short_code = input().lower()
      


        if   short_code == 'ca':
            print("create User Account")
            print('*' *50)

            print("Enter your user name")
            user_name = input()

            print("Email address..")
            email = input()

        while True:
            print("ep - enter passward:\n gp - to generate random passward")
            passward_choice == input().lower()
            if passward_choice == 'ep':
                passward = input("Enter passward\n")
                break
            elif passward_choice == 'gp':
                passward = generate_passward()
                break
            else:
                print("invalid try again")   

           

            
            save_user(create_user(user_name, email,passward))
            print('*' *50)
            print(f"Welcome {user_name} Your account is created successfully created proceed to the next step.")
            print('*' *50)
            

            elif short_code == 'lg':
            #login the user
            print('*' *50)
            print("Enter your user name..")
            user_name = input()

            print("Enter your passward....")
            passward = input()
            login = login_user(user_name, passward)
            if login_user(user_name,)

                elif short_code == 'da':
            if check_passward(user_name): #check if user exist
              if check_passward(user_name, passward):
                print("\n")
                print(f"Welcome{user_name}")
                print('*' *50)
                login_user == login:

            while True:
              print("Use these short codes:\n cc - Create a new credential, \n dc - display credential \n fc - find a credential \n gp - generate random passward \n d - delete credential \n ex - exit application \n")
                elif short_code = input().lower
                if short_code == "cc":
                print("Create New Credential")
                print("*" *50)
                print("Account name..")
                account = input().lower()
                print("Your  user name.... ")
                user_name = input()

        while True:
            print("ep: Enter passward if already have an account: \n gp - generate random passward")
        if passward_choice == 'ep':
            passward = input("Enter your passward\n")
        break
    elif passward_choice == 'gp':
            passward = generate_passward()
            break 
        else:
            print("invalid , try again")
            save_credential(create_new_credential(account, user_name, passward))
            print('\n')
            print(f"Account credential for : {account} user_name: {user_name} passward: {passward} successfully created")
            print('\n')
             elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
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
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
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
                search_credential.delete_credential()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} has successfully been generated")
        elif short_code == 'ex':
            print("Thanks for using pass-lock!")
            break
        else:
            print("Wrong entry try again")
    else:
        print("Enter valid input to proceed")

if __name__ == '__main__':
    passward_locker()


           


                    
          

           
                          
            



             









