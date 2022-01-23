from userDetails import UserAccount
from  credentialsDetails import  UserCredentials

def welcome():
    print('__  __  __  _____ ')
    print('|| / \\  || ||===')
    print('||//  \\ || ||=== ')
    print('|_/    \_| ||=== ')
welcome()
def createNewUserAccount(f_name,m_name,l_name,username,usermail,login_pass):
    newUserAccount = UserAccount(f_name,m_name,l_name,username,usermail,login_pass,)
    return newUserAccount
def saveUserAccount(userAccount):
    userAccount.saveUserAccount()
def displayUserAccount():
    return UserAccount.displayAccount()
def userLogin(username,login_pass):
    verifiedUserAccount = UserCredentials.userVerification(username,login_pass)
    return verifiedUserAccount
def createNewusercredential( myAccountName,username,login_pass):
    newUserCredential = UserCredentials(myAccountName,username,login_pass)    
    return newUserCredential
def saveUserCredential(userCredential):
    userCredential.saveUserCredential()

    
    

    
    