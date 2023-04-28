#A transaction class to send and receive money and test it.
#import random
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
import datetime
import collections
from Crypto.Signature import PKCS1_v1_5
from collections import OrderedDict

class Client:
    def __init__(self):
        random=Random.new().read
        self._private_key=RSA.generate(1024,random) #1024->key size
        self._public_key=self._private_key.publickey()
        self._signer=PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
    
class Transaction:
    def __init__(self,sender,receiver,value):
        self.sender=sender
        self.receiver=receiver
        self.value=value
        self.time=datetime.datetime.now()

    def to_dict(self):
        if self.sender=="Genesis":
            identity="Genesis"
        else:
            identity=self.sender.identity
        return collections.OrderedDict({
            "sender":identity,
            "receiver":self.receiver,
            "value":self.value,
            "time":self.time
        })
    def sign_tran(self):
        private_key=self.sender._private_key
        signer=PKCS1_v1_5.new(private_key)
        h=SHA.new(str(self.to_dict).encode('utf-8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
    
def display_tran(transaction):
    dict=transaction.to_dict()
    print('\nsender,Rifath--> \n'+dict['sender'])
    print('\nreceiver,Sara--> \n'+dict['receiver'])
    print('\nvalue--> \n'+str(dict['value']))
    print('\ntime--> \n'+str(dict['time']))
     
transactions=[]

Rifath=Client()
Sara= Client()

t1=Transaction(
Rifath,
Sara.identity,
15)

t1.sign_tran()
display_tran(t1)    


