# password protector
# pwordpro
# created by masoud mahjoubi

import useraccount as ua
import sqliteDrive as sd
import dencryption as dnc
import hashmake as hm
import color_print as clp
import UserInterface as ui

import os.path as op
import os
homedir = op.expanduser('~')
os.chdir(homedir + '/.local/etc/pwordpro')


uaccount = ua.accountjob()
hDrive = hm.hashing()
denText = dnc.dencryption()
dbDrive = sd.sqldrive()
uiInp = {'enc':denText, 'db':dbDrive}
userInt = ui.userinterface()
userInt.set_Dencrypt(denText)
userInt.set_DataBaseDrive(dbDrive)

dbKey = ''

print(clp.bcolors.HEADER + 'Welcome to PWordPro' + clp.bcolors.ENDC)
print(clp.bcolors.BOLD + 'You can save and retrieval your password safely' + clp.bcolors.ENDC)
print('\n')

appLock = 'close'
userAccount = {}

X = input('Signin [i] or Signup [u]? ')
if X=='i' or X=='I':
    userAcc = userInt.signInun('signin')
    if userAcc!=False:
        hashPass = hDrive.passwordHashing(userAcc['password'])
        userAccount['user'] = userAcc['username']
        userAccount['psswd'] = hashPass
        if uaccount.validationAccount(userAccount):
            appLock = 'open'
            dbKeyAdd = input('Enter DataBase key address file: ')
            dbKey = userInt.read_dbKey(dbKeyAdd)
            dbDrive._setUserName(userAccount['user'])
        else:
            print(clp.bcolors.WARNING + 'Account not exist !' + clp.bcolors.ENDC)
            appLock = 'close'
    else:
        print(clp.bcolors.WARNING + 'Password problem !' + clp.bcolors.ENDC)
elif X=='u' or X=='U':
    userAcc = userInt.signInun('signup')
    if userAcc!=False:
        hashPass = hDrive.passwordHashing(userAcc['password'])
        userAccount['user'] = userAcc['username']
        userAccount['psswd'] = hashPass
        uaccount.createAccount(userAccount)
        userInt.setUserName(userAccount['user'])
        dbKey = hDrive.keywordHashing(userAccount['user'])
        userInt.writeSecretKey(dbKey)
        appLock = 'open'
        dbDrive._setUserName(userAccount['user'])
    else:
        print(clp.bcolors.WARNING + 'Password problem !' + clp.bcolors.ENDC)
else:
    print(clp.bcolors.WARNING + 'None of the options selected' + clp.bcolors.ENDC)
    appLock = 'close'


if appLock=='open':
    denText.dencryptKey(dbKey)
    while(1):
        userInt.printmenu()
        SO = input('Please Selelct: ')
        clp.bcolors.clear()
        userInt.selectionHandling(SO)
elif appLock=='close':
    print(clp.bcolors.WARNING + 'you have not permission' + clp.bcolors.ENDC)
    exit()
else:
    print(clp.bcolors.WARNING + 'An unexpected problem has occurred' + clp.bcolors.ENDC)
    exit()
