import hashlib
import base64

from Crypto.Cipher import AES
from Crypto import Random

pad = lambda s: s + (32 - len(s) % 32) * chr(32 - len(s) % 32)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class CryptographyUtils:

    __key = None

    def __init__(self, passphrase: str):
        self.__key = hashlib.sha256(passphrase.encode("utf-8")).digest()


    def encrypt(self, messsage):
        """
        """
        messsage = pad(messsage)
        cipher = AES.new(self.__key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(messsage)).decode('utf-8')  


    def decrypt(self, token):
        """
        """ 
        decipher = AES.new(self.__key, AES.MODE_ECB)   
        return unpad(decipher.decrypt(base64.b64decode(token))).decode('utf-8')


    def hash(self, messsage):
        """
        """
        return base64.b64encode(hashlib.sha256(messsage.encode()).digest())