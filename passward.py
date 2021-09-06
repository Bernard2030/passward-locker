import random
import string

class User:
    """
    Class generates new instances of User
    """
    user_list = []

    def __init__(self, user_name,  passward):
        """
        Method defining user properties
        """

        self.user_name = user_name
        self.passward = passward
            

    def save_user(self):
        """
        A method which saves the new user instance on the user_list
        """

        User.user_list.append(self) 

    @classmethod
    def display_user(cls):
        """
        Method thad displays class user
        """
        return cls.user_list

    def delete_user(self):
        """
        delete method deletes a saved passward in our list_user
        """

        User.user_list.remove(self)
