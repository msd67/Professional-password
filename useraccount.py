# password protector
# useraccount
# created by masoud mahjoubi

def introModule():
    print("useraccount")

class accountjob:

    def __init__(self) -> None:
        self._username = ""
        self._passwd = ""
        self._truePasswd = ""
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def _accountCheck(self):
        with open('account') as f:
            lines = f.readlines()
            for line in lines:
                acc = line.split(':')
                if self._username==acc[0]:
                    self._truePasswd = acc[1]#.encode('utf-8')
                    return True
        return False


    def _pswdCheck(self):
        if self._truePasswd==self._passwd:
            return True
        return False
    
    def _setUser(self, usr: str="foo"):
        self._username = usr
    
    def _setPasswd(self, psdw: str):
        self._passwd = psdw

    def validationAccount(self, accnt: dict={"user":"foo", "psswd":"#"}):
        self._setUser(accnt["user"])
        self._setPasswd(accnt["psswd"])
        if self._accountCheck()==False:
            return False
        elif self._pswdCheck()==False:
            return False
        else:
            return True
    
    def createAccount(self, accnt: dict={"user":"foo", "psswd":"#"}):
        self._setUser(accnt["user"])
        if self._accountCheck()==False:
            line = accnt["user"] + ":" + accnt["psswd"] + ":\n"
            with open("account", 'a') as f:
                f.write(line)
            return True
        return False