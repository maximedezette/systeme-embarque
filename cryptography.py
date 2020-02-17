import hashlib
import base64

from Crypto.Cipher import AES
from Crypto import Random

pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

class Cryptography:

    key = "aaa"

    def __init__(self):
      token = self.encrypt("999975035:AAEegF-dcxF1KrUHeZKW9kvCG-fyt_y7e9E", "jhgkgkjvky")
      print(token)
      decode = self.decrypt(token,"jhgkgkjvky" )
      print(decode)


    def encrypt(self, messsage, passphrase):
        """
        """
        print(len(messsage))
        messsage = pad(messsage)
        print(len(messsage))
        key = hashlib.sha256(passphrase.encode('utf-8')).digest()
        cipher = AES.new(key, AES.MODE_ECB)
        msg = base64.b64encode(cipher.encrypt(messsage))
        return msg


    def hash(self, messsage):
        """
        """
        return base64.b64encode(hashlib.sha256(messsage.encode()).digest())


    def decrypt(self, token, passphrase):
        """
        """ 
        key = hashlib.sha256(passphrase.encode('utf-8')).digest()
        decipher = AES.new(key, AES.MODE_ECB)   
        return unpad(decipher.decrypt(base64.b64decode(token)))


crypto = Cryptography()