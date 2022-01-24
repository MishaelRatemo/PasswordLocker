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
    userAccount.saveUserAcc()
def displayUserAccount():
    return UserAccount.displayUser()
def userLogin(username,login_pass):
    verifiedUserAccount = UserCredentials.userVerification(username,login_pass)
    return verifiedUserAccount
def createNewusercredential( myAccountName,username,login_pass):
    newUserCredential = UserCredentials(myAccountName,username,login_pass)    
    return newUserCredential
def saveUserCredential(userCredential):
    userCredential.saveCredentials()

def delCredential(credentials):
    credentials.deleteUserCred()
def displayUserCredentials():
    return UserCredentials.displayUserCredentials()
def findUserCredentials(userAccount):
    return UserCredentials.findUsercredential(userAccount)
def doCredentialsExist(account):
    return UserCredentials.doCredentialsExist(account)
def copyPass(userAccount):
    return UserCredentials.copyLoginPass(userAccount)
def systemGeneratedPassword():
    autoGenRandPass = UserCredentials.genRandPass()
    return autoGenRandPass

 #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
def myPasswordLocker():
    print('**********$$$$$$******$$$$$$*******$$$$$$********\n\n')
    print('**********Welcome to your password Database******\n')
    print('May I know your Name?  ')
    username= input()
    print(f'Hi <<< {username} >>> To Start, key in any of the following commands')
    print('        CA ====> to create New User Account')
    print('        LI ===> to  Login In to existing Account')
    comands= input('').upper().strip()
    if comands == 'CA':
        print('^'*5 + ' '+ 'Sign Up '+ '^'*5)
        print('-'*12)
        f_name = input('Enter Your First Name: ')
        m_name = input('Enter Your Middle Name: ')
        l_name = input('Enter Your Last Name: ')
        usermail = input('Enter Your Email: ')
        username= input('Enter preffered Username: ')
        while True:
            print('     MP ===> To enter your password')
            print('     Gp ===> System Generated Password')
            command= input('').upper().strip()
            if command == 'MP':
                login_pass= input('PLease Enter password')
                break
            elif command == 'GP':
                login_pass= systemGeneratedPassword()
                break
            else:
                print('Ooops!!! Incorrect Choice...... Retry')
        saveUserAccount(createNewUserAccount(f_name,m_name,l_name,username,usermail,login_pass))
        print('*'*30)
        print(f'*'*10 +f' Thank you {username}.  You have successfully signed up '+ '*'*10 )
        displayUserAccount()
    elif comands =='LI':
        print('^'*30)
        print('Enter username and password to sign in: ')
        username= input('Username:  ')
        login_pass= input('Password:  ')
        userlogins = userLogin(username,login_pass)
        if userLogin == userlogins:
            print(f'Hi, {username}. Welcome back to PasswordLocker\n\n')
    while True:
        print('Please key in any of the following to proceed \n')
        print('CC ===> Create new user Credential')
        print('DC ===> Display existing Account credentials')
        print('FC ===> Find User Credential')
        print('GP ===> Auto generated Password')
        print('DEL===> Delete account credential')
        print('X ===> Exit application')
        command= input().upper().strip()
        if command == 'CC':
            print('Create new user Account Credential')
            print('-'*30)
            print('Enter account Name :   ')
            userAccountName = input().upper().strip()
            print('Username for above account')
            accUsername =input().strip()
            while True:
                print('1 ===> Type Password(existing) ')
                print('2 ===> system Generated Password')
                p_choice= input().strip()
                if p_choice == '1':
                    password = input('Type Password : ')
                    break
                elif p_choice == '2':
                    password= systemGeneratedPassword()
                    break
                else:
                    print(' Incorrect command choice. Try again')
            saveUserCredential(createNewusercredential(userAccountName,accUsername,password))
            print('')
            print(f'Credential for <<< {userAccountName} >>>  .. Username << {accUsername} >> and Password < {password} > have been successfully ')
            print('\n')
        elif command == 'DC' :
            if displayUserCredentials():
                print('Available Accounts :')
                print('')
                for acc in displayUserCredentials():
                    print(f'Acc : {acc.myAccount}')
                    print(f'Username: {username}')
                    print(f'Password: {password}')
                    print(' ')
                print('---'*10)
            else:
                print('NO Credentials saved yet ')
        elif command == 'FC':
            print('Enter account to find : ')
            accountName = input().upper().strip
            if findUserCredentials(accountName):
                searchAcc = findUserCredentials(accountName)
                print(f'Account : <<< {searchAcc.myAccount} >>> \n')
                print(f'Username: <<< { searchAcc.username} >>> \n')
            else:
                print(f'accountName doesnt exist \n')
        elif command == 'GP':
            password = systemGeneratedPassword()
            print(f'Your generated password is : <<< {password} >>>')
        elif command == 'DEL':
            print('Enter Account to Delete ')
            accountName = input().upper().strip()
            if findUserCredentials(accountName):
                searchAcc = findUserCredentials(accountName)
                print('')
                searchAcc.deleteUserCred()
                print(f'{ searchAcc.myAccount} deleted successfully \n')
            else:
                print(f'{accountName} cannot be deleted because it does not exist \n')
        elif command == 'X':
            print(' Thank for trusting Us. See you next time. Nice time\n\n '+'=*'*20 +'\n')
            break
        else:
            print('Oooops!!! Invalid command. Retry')
                
    
if __name__ == '__main__':
    myPasswordLocker()
    
    
    
    
    
        
    

    
    