import unittest
from passward import User

class TestOne(unittest.TestCase):
    """
    A test One that defines test cases for the User class.
    """

def setUp(self):
    """
    A method that runs before the user test method runs
    """    

    self.new_user = User("BernardOpiyo", "Bro@xyz2030", "brobernard.254@gmail.com")