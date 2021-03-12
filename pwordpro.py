# password protector
# pwordpro
# created by masoud mahjoubi

import getpass
import useraccount as ua
import sqliteDrive as sd
import dencryption as dnc
import hashmake as hm
import color_print as clp


uaccount = ua.accountjob()
hDrive = hm.hashing()
denText = dnc.dencryption()
dbDrive = sd.sqldrive()

dbKey = ''

def signInun()->dict:
    signInfo = {}
    signInfo['username'] = input('Please enter username: ')
    signInfo['password'] = getpass.getpass()
    return signInfo

def questionnaire()->dict:
    accountInfo = {}
    print(clp.bcolors.RED + '\n' + clp.bcolors.ENDC)
    accountInfo['id'] = input('Enter ID: ')
    accountInfo['key'] = input('Enter KEYWORD: ')
    accountInfo['user'] = input('Enter USERNAME: ')
    psswdAcc = getpass.getpass()
    accountInfo['pass'] = denText.encryptMessage(psswdAcc)
    accountInfo['link'] = input('Enter LINK: ')
    accountInfo['describe'] = input('Enter some DESCRIBE: ')
    return accountInfo

def writeSecretKey(key: str):
    with open("SecPassKey01", 'w') as f:
        f.write(key)

def read_dbKey(keyAdd: str):
    with open(keyAdd) as f:
        key = f.readline()
    return key

print(clp.bcolors.HEADER + 'Welcome to PWordPro' + clp.bcolors.ENDC)
print(clp.bcolors.BOLD + 'You can save and retrieval your password safely' + clp.bcolors.ENDC)
print('\n')

appLock = 'close'
userAccount = {}

X = input('Signin [i] or Signup [u]? ')
if X=='i' or X=='I':
    userAcc = signInun()
    hashPass = hDrive.passwordHashing(userAcc['username'])
    userAccount['user'] = userAcc['username']
    userAccount['psswd'] = hashPass
    if uaccount.validationAccount(userAccount):
        appLock = 'open'
        dbKeyAdd = input('Enter DataBase key address file: ')
        dbKey = read_dbKey(dbKeyAdd)
    else:
        print(clp.bcolors.WARNING + 'Account not exist !' + clp.bcolors.ENDC)
        appLock = 'close'
elif X=='u' or X=='U':
    userAcc = signInun()
    hashPass = hDrive.passwordHashing(userAcc['username'])
    userAccount['user'] = userAcc['username']
    userAccount['psswd'] = hashPass
    uaccount.createAccount(userAccount)
    dbKey = hDrive.keywordHashing(userAccount['user'])
    writeSecretKey(dbKey)
    appLock = 'open'
else:
    print(clp.bcolors.WARNING + 'None of the options selected' + clp.bcolors.ENDC)
    appLock = 'close'


if appLock=='open':
    denText.dencryptKey(dbKey)
    newInputAcc = questionnaire()
    dbDrive.insertData(newInputAcc)
    Q = input('Do you want read all account[y/n]? ')
    if Q=='y' or Q=='Y':
        records = dbDrive.readAllData()
        print('\n')
        if records:
            for row in records:
                print('ID: \t\t', row[0])
                print('Keyword: \t', row[1])
                print('User Name: \t', row[2])
                print('Password: \t', denText.decryptMessage(row[3]))
                print('Link: \t\t', row[4])
                print('Description: \t', row[5])
                print('\n')
    print('See you later')
    exit()
elif appLock=='close':
    print(clp.bcolors.WARNING + 'you have not permission' + clp.bcolors.ENDC)
    exit()
else:
    print(clp.bcolors.WARNING + 'An unexpected problem has occurred' + clp.bcolors.ENDC)
    exit()
