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

def tearDown(self):
    """
    A method that cleans after each test case is run
    """
    User.user_list = []

def test__init__(self):
    """
    TestCase to test if the object is initialized as required.
    """
    self.assertEqual(self.new_user.user_name, "BernardOpiyo")
    self.assertEqual(self.new_user.passward, "Bro@xyz2030")
    self.assertEqual(self.new_user.email, "brobernard.254@gmail.com")

def test_save_user(self):
    """
    test case to test if the uder object is saved into the user_list
    """

    self.new_user.save_user()
    self.assertEqual(len(User.user_list), 1)

def test_save_multiple_users(self):
    """
    Test to check if we can save more than one user
    """
    self.new_user.save_user()
    test_user = User("Test", "user", "test@user.com")
    test_user.save_user()
    self.assertEqual(len(User.user_list), 2) 

def test_display_users(self):
    """
    Method to return a list of users
    """  

    self.assertEqual(User.dispalay_users(),User.user_list)


if __name__ == '__main__':
    unittest.main()    

           