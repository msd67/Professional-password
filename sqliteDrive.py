# password protector
# sqliteDrive
# created by masoud mahjoubi

import sqlite3
import os.path as op

def introModule():
    print("sqliteDrive")

class sqldrive():

    def __init__(self) -> None:
        self._tableName = 'passwords'
        self._tableBase = 'passwords'
        self._dbName = 'securityPass.db'
        self._keySrch = ''
        self._record = ''
        self._dataTable = []
        self._numReco = None
        self._username = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def _commCreate(self, act: str, fld: str):
        comm = ''
        if act=='tableExist':
            comm = 'CREATE TABLE IF NOT EXISTS ' + self._tableName + ' '
            comm += '(ID    INT PRIMARY KEY NOT NULL,'
            comm += 'KYW    TEXT    NOT NULL,'
            comm += 'USER   TEXT    NOT NULL,'
            comm += 'PASS   TEXT    NOT NULL,'
            comm += 'LINK   TEXT    NOT NULL,'
            comm += 'DESCRIBE   TEXT);'
        elif act=='insertRecord':
            comm = 'INSERT INTO ' + self._tableName
            comm += ' (ID,KYW,USER,PASS,LINK,DESCRIBE) VALUES ('
            comm += self._record['id'] + ',\''
            comm += self._record['key'] + '\',\''
            comm += self._record['user'] + '\',\''
            comm += self._record['pass'] + '\',\''
            comm += self._record['link'] + '\',\''
            comm += self._record['describe'] + '\''
            comm += ');'
        elif act=='recordExist':
            comm = 'SELECT ID FROM ' + self._tableName
            comm += ' WHERE KYW = \''
            comm += self._keySrch + '\''
        elif act=='readAllRecords':
            comm = 'SELECT ID, KYW, USER, PASS, LINK, DESCRIBE FROM ' + self._tableName
        elif act=='numberOfRecords':
            comm = 'SELECT COUNT(*) FROM ' + self._tableName + ';'
        elif act=='fieldBasedSearch':
            if fld=="ID":
                comm = 'SELECT ID, KYW, USER, PASS, LINK, DESCRIBE FROM ' + self._tableName
                comm += ' WHERE ID = '
                comm += self._keySrch
            elif fld in ['KYW', 'USER', 'PASS', 'LINK']:
                comm = 'SELECT ID, KYW, USER, PASS, LINK, DESCRIBE FROM ' + self._tableName
                comm += ' WHERE '
                comm += fld + ' = \''
                comm += self._keySrch + '\''
            else:
                print('No field selected')
        elif act=='updateData':
            comm = 'UPDATE ' + self._tableName + ' set '
            comm += 'KYW = \'' + self._record['key'] + '\','
            comm += 'USER = \'' + self._record['user'] + '\','
            comm += 'PASS = \'' + self._record['pass'] + '\','
            comm += 'LINK = \'' + self._record['link'] + '\','
            comm += 'DESCRIBE = \'' + self._record['describe'] + '\''
            comm += 'WHERE ID = ' + self._record['id']
        elif act=='deleteData':
            comm = 'DELETE FROM ' + self._tableName + ' WHERE ID = ' + self._keySrch
        else:
            print('No action selected')
        return comm

    def _setkeySearch(self, key):
        self._keySrch = key

    def _setRecord(self, rcrd):
        self._record = rcrd
    
    def _setUserName(self, uname: str):
        self._username = uname
        self._tableName = self._tableBase + '_' + self._username

    def _numberOfRecords(self, conn):
        comm = self._commCreate('numberOfRecords', '')
        nor = conn.execute(comm)
        return nor.fetchone()[0]

    def _tableExist(self, conn):
        comm = self._commCreate('tableExist', '')
        conn.execute(comm)

    def _recordExist(self, conn):
        print('[INFO] function recordExist')
        comm = self._commCreate('recordExist', '')
        cursor = conn.execute(comm)
        recID = 0
        if cursor!='':
            for row in cursor:
                return row[0]
        return recID
    
    def _readAllRecords(self, conn):
        comm = self._commCreate('readAllRecords', '')
        return conn.execute(comm)
    
    def _insertRecord(self, conn):
        print('[INFO] function insertRecord')
        comm = self._commCreate('insertRecord', '')
        conn.execute(comm)
        conn.commit()
    
    def _specificRecords(self, conn, fld):
        print('[INFO] function specificRecords')
        comm = self._commCreate('fieldBasedSearch', fld)
        return conn.execute(comm)
    
    def _insertProcess(self, conn):
        print('[INFO] function insertProcess')
        rcdExist = self._recordExist(conn)
        if rcdExist==0:
            print('[Info] Record Not Exist')
            self._insertRecord(conn)
        else:
            print('[Info] Record Exist ' + str(rcdExist))
    
    def _updateRecords(self, conn):
        print('[INFO] function updateRecords')
        comm = self._commCreate('updateData', '')
        conn.execute(comm)
        conn.commit()
    
    def _deleteRecord(self, conn):
        print('[INFO] function deleteRecord')
        comm = self._commCreate('deleteData', '')
        conn.execute(comm)
        conn.commit()
    
    def insertData(self, rcd: dict):
        self._setRecord(rcd)
        self._setkeySearch(rcd['key'])
        try:
            conn = sqlite3.connect(self._dbName)
            self._tableExist(conn)
            self._insertProcess(conn)
        except Exception as e:
            print('[Err] DataBase error ocurred')
            print(e)
        finally:
            conn.close()
    
    def _readAllDataProcess(self):
        try:
            conn = sqlite3.connect(self._dbName)
            records = self._readAllRecords(conn)
        except Exception as e:
            self._dataTable = []
            print('[Err] DataBase error ocurred')
            print(e)
        else:
            for row in records:
                self._dataTable.append(row)
        finally:
            conn.close()
    
    def _numberOfDataProcess(self):
        try:
            conn = sqlite3.connect(self._dbName)
            self._numReco = self._numberOfRecords(conn)
        except Exception as e:
            self._numReco = None
            print('[Err] DataBase error ocurred')
            print(e)
        finally:
            conn.close()
    
    def _specificDataProcess(self, fld):
        try:
            conn = sqlite3.connect(self._dbName)
            records = self._specificRecords(conn, fld)
        except Exception as e:
            self._dataTable = []
            print('[Err] DataBase error ocurred')
            print(e)
        else:
            for row in records:
                self._dataTable.append(row)
        finally:
            conn.close()
    
    def _updateDataProcess(self):
        try:
            conn = sqlite3.connect(self._dbName)
            self._updateRecords(conn)
        except Exception as e:
            print('[Err] DataBase error ocurred, when updateDataProcessing')
            print(e)
        finally:
            conn.close()
    
    def _deleteDataProcess(self):
        try:
            conn = sqlite3.connect(self._dbName)
            self._deleteRecord(conn)
        except Exception as e:
            print('[Err] DataBase error ocurred, when deleteDataProcessing')
            print(e)
        finally:
            conn.close()
    
    def readAllData(self):
        self._dataTable = []
        self._readAllDataProcess()
        return self._dataTable
    
    def numberOfData(self):
        self._numReco = None
        self._numberOfDataProcess()
        return self._numReco
    
    def specificData(self, field: str='KYW', keyw: str=''):
        if keyw!='':
            self._dataTable = []
            self._setkeySearch(keyw)
            self._specificDataProcess(field)
            return self._dataTable
        return []
    
    def updateData(self, rcd: dict):
        self._setRecord(rcd)
        self._updateDataProcess()
    
    def deleteData(self, id: str='0'):
        self._setkeySearch(id)
        self._deleteDataProcess()




