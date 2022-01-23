import unittest
from userDetails import  UserAccount
# from credentialsDetails import Credentials

class TestUserAccount (unittest.TestCase):
    '''
    Test class that defines test cases for the UseAccount class behaviours.
    '''
    def setUp(self):
        '''
        set up method to run before individual test cases
        '''
        self.newUserAccount = UserAccount ("Mishael","Mosoti","Ratemo","Mismora","ratemomishael@gmail.com","Pxjs3$12")
     
     #*************************************************************#
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''   
        UserAccount.userAccounts=[]   
     #*************************************************************#
    def test_init(self):
        '''
         test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.newUserAccount.f_name,'Mishael')
        self.assertEqual(self.newUserAccount.m_name,'Mosoti')
        self.assertEqual(self.newUserAccount.l_name,'Ratemo')
        self.assertEqual(self.newUserAccount.username,'Mismora')
        self.assertEqual(self.newUserAccount.usermail,'ratemomishael@gmail.com')
        self.assertEqual(self.newUserAccount.login_pass,'Pxjs3$12')
        
      #*************************************************************#  
    def test_saveUserAcc(self):
        '''
        test case to test if a new user acc instance has been saved into the UserAcc Array
        '''
        self.newUserAccount.saveUserAcc()
        self.assertEqual(len(UserAccount.userAccounts),1)
        
     #*************************************************************#  
    def test_saveMultipleAccounnts(self):
        '''
        Method  to check if we can save user acc objects to our user account array
        NB: method does not have to exist in UserAccount class
        '''
        self.newUserAccount.saveUserAcc()
        testUserAcc = UserAccount('TestUserFirstname','TestUserMiddleName','TestUserLastName','TestUsername', 'test@gmail.com','testPassword')
        testUserAcc.saveUserAcc()
        self.assertEqual(len(UserAccount.userAccounts),2)
        
     #*************************************************************#  
    def test_deleteUserAccount(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list        
        '''
        self.newUserAccount.saveUserAcc()
        testUserAcc = UserAccount('TestUserFirstname','TestUserMiddleName','TestUserLastName','TestUsername', 'test@gmail.com','testPassword')
        testUserAcc.saveUserAcc()
        self.newUserAccount.deleteUserAcc()
        self.assertEqual(len(UserAccount.userAccounts),1)
     #*************************************************************#
    
        
        
        
        
              
        
        
if __name__ == '__main__':
    unittest.main()
        