import unittest
from credentials import Credential

class TestOne(unittest.TestCase):

    def setUp(self):
        """
        Method to run before any other test case
        """

        self.new_credential = Credential("user_name", "email", "passward" )

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
    self.assertEqual(self.new_credential.email, "email")
    self.assertEqual(self.new_credential.passward, "passward")
    

def save_credential(self):
    """
    test case to check if credential object is saved in the credential list
    """    

    self.new_credential.save_credential()
    self.assertEqual(len(Credential.credential_list), 1)

def credential_available(self):
    """
    test to check if we can return a boolean depending on availability of a credential
    """    
    self.new_credential.save_credential()
    my_credential = Credential("magnet", "ben10", "Wx123")
    my_credential.save_credential()
    credential_exist = Credential.if_credential_available("magnet", "ben10", "Wx123")
    self.assertTrue(credential_exist)
def display_credential(self):
    """
    test to display saved credentials
    """       

    self.assertEqual(Credential.display_credential(), Credential.credential_list)

if __name__ == '__main__':
    unittest.main()    
