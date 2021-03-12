# password protector
# keycreate
# created by masoud mahjoubi

import hashlib
import os

def introModule():
    print("hashmake")

class hashing:

    def __init__(self) -> None:
        self._inputStr = 'pwordpro'
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def _setInputStr(self, strWord: str='keycreate'):
        self._inputStr = strWord

    def _passwordHashingProcess(self):
        salt = '97867564passwordProfessional(!@#)'.encode('utf-8')
        key = hashlib.pbkdf2_hmac(
            'sha256', # The hash digest algorithm for HMAC
            self._inputStr.encode('utf-8'), # Convert the password to bytes
            salt, # Provide the salt
            100000, # It is recommended to use at least 100,000 iterations of SHA-256 
            dklen=128 # Get a 128 byte key
        )
        return key

    def _keywordHashingProcess(self):
        salt = os.urandom(32) # Remember this
        key = hashlib.pbkdf2_hmac(
            'sha256', # The hash digest algorithm for HMAC
            self._inputStr.encode('utf-8'), # Convert the password to bytes
            salt, # Provide the salt
            100000, # It is recommended to use at least 100,000 iterations of SHA-256 
            dklen=16 # Get a 32 byte key
        )
        return key

    def passwordHashing(self, psswd: str='hashmake'):
        self._setInputStr(psswd)
        return self._passwordHashingProcess().hex()

    def keywordHashing(self, key: str='hashmake'):
        self._setInputStr(key)
        return self._keywordHashingProcess().hex()


