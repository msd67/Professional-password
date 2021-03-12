# password protector
# dencryption
# created by masoud mahjoubi

from cryptography.fernet import Fernet 
import base64

def introModule():
    print("dencryption")


class dencryption:

    def __init__(self) -> None:
        self._message = None
        self._encMessage = None
        self._fernet = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def _setKey(self, key: str):
        # The length of the input string should be 32
        prepareKey = base64.b64encode(key.encode("utf-8"))
        self._fernet = Fernet(prepareKey)
    
    def _setMessage(self, msg: str):
        self._message = msg
    
    def _setEncMessage(self, enc_msg: str):
        self._encMessage = enc_msg
    
    def _encMessageProcess(self):
        return self._fernet.encrypt(self._message.encode())
    
    def _decMessageProcess(self):
        #prepareMSG = base64.b64encode(self._encMessage.encode("utf-8"))
        prepareMSG = self._encMessage.encode('utf-8')
        return self._fernet.decrypt(prepareMSG).decode()

    def dencryptKey(self, key: str):
        self._setKey(key)

    def encryptMessage(self, msg: str):
        self._setMessage(msg)
        enMessage = self._encMessageProcess()
        #return enMessage.hex()
        return enMessage.decode('utf-8')

    def decryptMessage(self, enc_msg: str):
        self._setEncMessage(enc_msg)
        return self._decMessageProcess()
