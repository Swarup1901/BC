print("Rifath,3")
import hashlib

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message,difficulty=1):
    assert difficulty>=1 #debugging
    prefix= '1'* difficulty #verify diffficulty
    print ("prefix",prefix)
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        print("Testing --> " + digest)
        if digest.startswith(prefix):
            print("After" + str(i) + "iterations found nounce" + digest)
            return i
mine("Rifath", 3)
