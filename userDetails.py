class UserAccount:
    '''
    User Class for creating user accounts and saving user details
    '''
    userAccounts=[]
    def __init__(self,f_name,m_name,l_name,username,usermail,login_pass):
        #instanciatiation 
        self.f_name = f_name # user's first name
        self.m_name = m_name # user's middle name
        self.l_name = l_name # user's last name
        self.username=username # user's preferred login username
        self.usermail = usermail
        self.login_pass=login_pass
     #-----------------------------------------------------------------------------#        
    def saveUserAcc(self):
        '''
        method to save new users into users array
        '''
        UserAccount.userAccounts.append(self)
     #-----------------------------------------------------------------------------#
    def deleteUserAccount(self):
        '''
        Method to delete user account(Account must exist first)
        '''
        UserAccount.userAccounts.remove(self)
     #-----------------------------------------------------------------------------#
    @classmethod   
    def displayUser(cls):
        '''
        Method returning a user from the list
        '''
        return cls.userAccounts
        
        
    
        
              
        