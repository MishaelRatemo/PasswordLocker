
import string,random
# import pyperclip
from userDetails import UserAccount
class UserCredentials:
    ''' Create credentials class to help create new objects of credentials   '''
    credentials=[]
    @classmethod
    def userVerification(cls,username,login_pass):
        '''
        method to verify whether the user Account is in our userAccounts Array or not        
        '''
        _user = ''
        for user in UserAccount.userAccounts:
            if user.username == username and user.login_pass ==login_pass:
                _user == user.username
        return _user
     #-----------------------------------------------------------------------------# 
    def __init__(self,myAccount,username,login_pass):
        '''function that instantiates userAccount credentials to be stored'''
        self.myAccount = myAccount        
        self.username = username
        self.login_pass=login_pass
        
     #-----------------------------------------------------------------------------# 
    def saveCredentials(self):
        '''Method to store new user credentilals to array'''        
        UserCredentials.credentials.append(self)
     #-----------------------------------------------------------------------------# 
    def deleteUserCred(self):
        ''' funtion to delete user account credentials from credeentials Array'''
        UserCredentials.credentials.remove(self)
     #-----------------------------------------------------------------------------#
    
    def genRandPass(passwordlen=10):
        '''Auto generate password containing digits,alphabets both in lower and Uppercase of length 10 characters'''
        userPassword = string.ascii_letters  + string.digits
        return "".join(random.choice(userPassword)
                       for char in range(passwordlen)
                       )
     #-----------------------------------------------------------------------------#
    @classmethod
    def findUsercredential(cls,userAccount):
        '''This method finds user credential that matches account name  passed in'''
        for userCredential in cls.credentials:
            if userCredential.myAccount == userAccount:
                return userCredential
    #-----------------------------------------------------------------------------#
    @classmethod
    def doCredentialsExist(cls,account):
        ''' this checks if user credentials exists in the credentials array'''
        for item in cls.credentials:
            if item.myAccount == account:
                return True
        return False 
    #-----------------------------------------------------------------------------#                       
    @classmethod
    def displayUserCredentials(cls):
        ''' this return a list of existing user creddentials'''
        return cls.credentials
     #-----------------------------------------------------------------------------#
    @classmethod
    def copyLoginPass(cls,userAccount):
        credFound = UserCredentials.findUsercredential(userAccount)
        pyperclip.copy(credFound.login_pass)
        
        
    
        
            
        
        
        
        
        