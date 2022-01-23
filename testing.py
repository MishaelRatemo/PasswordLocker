from operator import le
import unittest
from userDetails import  UserAccount
from credentialsDetails import UserCredentials

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
        self.newUserAccount.deleteUserAccount()
        self.assertEqual(len(UserAccount.userAccounts),1)
        
 #*******---------------************----------------********************#
class TestUserCredentials(unittest.TestCase):
    def setUp(self):
        ''' method to run before individual test cases run'''
        self.newUserCredential =UserCredentials('twitter','@Mishael','mixxy@123')
    
     #*************************************************************#  
    def tearDown(self):
        '''tearDown method that does clean up after each test case has run. '''   
        UserCredentials.credentials=[]
        
     #*************************************************************#         
    def test_init(self):
         '''test_init test case to test if the new user cred..ls is inistantiated properly'''
         self.assertEqual(self.newUserCredential.myAccount,'twitter')
         self.assertEqual(self.newUserCredential.username,'@Mishael')
         self.assertEqual(self.newUserCredential.login_pass,'mixxy@123')
     #*************************************************************#  
    def test_saveCredentials(self):
        self.newUserCredential.saveCredentials()
        self.assertEqual(len(UserCredentials.credentials),1)
     #*************************************************************#  
    def testSaveMultipleUserAcc(self):
        ''' testing if we can save many user acc credentials'''
        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('instagram','Ratemo','insta@#4')
        testUserCredential.saveCredentials()
        self.assertEqual(len(UserCredentials.credentials),2)
     #*************************************************************#  
    def test_deleteUserCred(self):
        ''' testing if we can actully delete user acc credentials''' 
        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('instagram','Ratemo','insta@#4')
        testUserCredential.saveCredentials()
        self.newUserCredential.deleteUserCred()
        self.assertEqual(len(UserCredentials.credentials),1)
     #*************************************************************#   
    def test_doCredentialsExist(self):
        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('instagram','Ratemo','insta@#4')
        testUserCredential.saveCredentials()
        userCredentialExist= UserCredentials.doCredentialsExist('instagram')
        self.assertTrue(userCredentialExist)  
    def test_findUsercredential(self):
        '''testing if user can actually find a user acc credential'''
        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('instagram','Ratemo','insta@#4')
        testUserCredential.saveCredentials()
        userCred = UserCredentials.findUsercredential('instagram')
        self.assertEqual(userCred.myAccount, testUserCredential.myAccount)
        
        
         
         
         
        
        
            
        
        

        
        
        
        
              
        
        
if __name__ == '__main__':
    unittest.main()
        