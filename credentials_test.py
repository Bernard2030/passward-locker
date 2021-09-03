import unittest
from credentials import Credential

class TestOne(unittest.TestCase):

    def setUp(self):
        """
        Method to run before any other test case
        """

        self.new_credential = Credential("user_name", "passward", "email")

def tearDown(self):
    """
    Method does clean-up after each test has run
    """        

    Credential.credential_list = []

def test__init__(self):
    """
    test case to test if the object property is correctly initialized
    """    
    self.assertEqual(self.new_credential.use_name, "user_name")
    self.assertEqual(self.new_credential.passward, "passward")
    self.assertEqual(self.new_credential.email, "email")

def test_save_credential(self):
    """
    test case to check if credential object is saved in the credential list
    """    

    self.new_credential.save_credential()
    self.assertEqual(len(Credential.credential_list), 1)
def test_display_credential(self):
    """
    test to display saved credentials
    """       

    self.assertEqual(Credential.display_credential(), Credential.credential_list)

if __name__ == '__main__':
    unittest.main()    