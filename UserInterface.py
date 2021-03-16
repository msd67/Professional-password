# password protector
# validation
# created by masoud mahjoubi

import getpass

class userinterface():

    def __init__(self) -> None:
        self._dencrypt = None
        self._dbDrive = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def set_Dencrypt(self, enc):
        self._dencrypt = enc
    
    def set_DataBaseDrive(self, db):
        self._dbDrive = db
    
    def _questionnaire(self)->dict:
        accountInfo = {}
        accountInfo['id'] = input('Enter ID: ')
        accountInfo['key'] = input('Enter KEYWORD: ')
        accountInfo['user'] = input('Enter USERNAME: ')
        psswdAcc = getpass.getpass()
        accountInfo['pass'] = self._dencrypt.encryptMessage(psswdAcc)
        accountInfo['link'] = input('Enter LINK: ')
        accountInfo['describe'] = input('Enter some DESCRIBE: ')
        return accountInfo
    
    def _insertHandle(self):
        newRecord = self._questionnaire()
        self._dbDrive.insertData(newRecord)
    
    def _searchHandle(self):
        options = ['ID', 'KYW', 'USER', 'PASS', 'LINK']
        print('1-ID, 2-KEY, 3-USER, 4-PASS, 5-LINK')
        SO = int(input('Please select field search: '))
        fld = options[SO-1]
        srch_vlu = input('Enter value: ')
        if fld=='PASS':
            srch_vlu = self._dencrypt.encryptMessage(srch_vlu)
        return self._dbDrive.specificData(fld, srch_vlu)
    
    def _showAllHandle(self):
        return self._dbDrive.readAllData()
    
    def _deleteHandle(self):
        id = input('Enter account id: ')
        self._dbDrive.deleteData(id)
    
    def _exportHandle(self):
        so = input('Normally or Raw [N/R]: ')
        if so=='N' or so=='n':
            rcds = self._showAllHandle()
            with open('passwd_Nrm.EXT', 'w') as f:
                for rcd in rcds:
                    f.write('ID:\t\t' + str(rcd[0]) + '\n')
                    f.write('Keyword:\t' + rcd[1] + '\n')
                    f.write('User Name:\t' + rcd[2] + '\n')
                    f.write('Password:\t' + self._dencrypt.decryptMessage(rcd[3]) + '\n')
                    f.write('Link:\t\t' + rcd[4] + '\n')
                    f.write('Description:\t' + rcd[5] + '\n')
                    f.write('\n')
        elif so=='R' or so=='r':
            rcds = self._showAllHandle()
            with open('passwd_Raw.EXT', 'w') as f:
                for rcd in rcds:
                    f.write(str(rcd[0]) + '\n')
                    f.write(rcd[1] + '\n')
                    f.write(rcd[2] + '\n')
                    f.write(self._dencrypt.decryptMessage(rcd[3]) + '\n')
                    f.write(rcd[4] + '\n')
                    f.write(rcd[5] + '\n')
        else:
            print('No options selected')

    def _showRecords(self, records):
        if records:
            print('')
            for row in records:
                print('ID: \t\t', row[0])
                print('Keyword: \t', row[1])
                print('User Name: \t', row[2])
                print('Password: \t', self._dencrypt.decryptMessage(row[3]))
                print('Link: \t\t', row[4])
                print('Description: \t', row[5])
                print('\n')

    def signInun(self)->dict:
        signInfo = {}
        signInfo['username'] = input('Please enter username: ')
        signInfo['password'] = getpass.getpass()
        return signInfo

    def writeSecretKey(self, key: str):
        with open("SecPassKey01", 'w') as f:
            f.write(key)

    def read_dbKey(self, keyAdd: str):
        with open(keyAdd) as f:
            key = f.readline()
        return key

    def printmenu(self):
        print('1- Insert new password account')
        print('2- Search')
        print('3- Show all account')
        print('4- Delete')
        print('5- Export')
        print('6- Exit')
    
    def selectionHandling(self, SO):
        if SO=='1':
            # Insert
            self._insertHandle()
        elif SO=='2':
            # Search
            rcd = self._searchHandle()
            self._showRecords(rcd)
        elif SO=='3':
            # Show all records
            rcd = self._showAllHandle()
            self._showRecords(rcd)
        elif SO=='4':
            # Delete
            self._deleteHandle()
        elif SO=='5':
            # Export
            self._exportHandle()
        elif SO=='6':
            # Exit
            print('\nExit Selected')
            exit()
        else:
            print('No option selected!')

