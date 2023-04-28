from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
import datetime
import binascii
from collections import OrderedDict
import collections
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
class Client:
    def __init__(self):
        random = Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
class Transaction:
    def __init__(self, sender, recipent, value):
        self.sender = sender
        self.recipent = recipent
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            'sender': identity,
            'recipent': self.recipent,
            'value': self.value,
            'time': self.time
        })
    def sign_tran(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
def display_transaction(transaction):
    # for transaction in transactions:
    dict = transaction.to_dict()
    print("sender:" + dict['sender'])
    print('-----')
    print("recipent:" + dict['recipent'])
    print('-----')
    print("value:" + str(dict['value']))
    print('-----')
    print("time:" + str(dict['time']))
    print('-----')
transactions = []
Rifath = Client()
Armeen = Client()
Sara = Client()

t1 = Transaction(
    Rifath,
    Armeen.identity,
    15.0
)
t1.sign_tran()
transactions.append(t1)
t2 = Transaction(
    Armeen,
    Sara.identity,
    17.0
)
t2.sign_tran()
transactions.append(t2)
t3 = Transaction(
    Sara,
    Armeen.identity,
    10.0
)
t3.sign_tran()
transactions.append(t3)
tn = 1
for t in transactions:
    print("Transaction: ", tn)
    display_transaction(t)
    tn = tn + 1
    print('-------------------')
