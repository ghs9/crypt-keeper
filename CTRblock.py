import Crypto.Cipher.AES
import Crypto.Util.Counter

key = "0123456789ABCDEF"
from Crypto.Hash import SHA256
from Crypto import Random

nonce = Random.new().read(16)
key = SHA256.new(key+nonce).digest()
iv = "0000000000009001"
plaintext = ""
with open('pg10.txt', 'r') as file:
    for line in file:
        plaintext += line



# print plaintext



# plaintext = "Attack at dawn" # replace with gutenberg

ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))

cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CTR, counter=ctr)
encrypted = cipher.encrypt(plaintext)
file = open("encryptedCTR.txt", 'w+')
file.write(encrypted)

ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
strng = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CTR, counter=ctr).decrypt(encrypted)

file = open("decryptedCTR.txt", 'w=')
file.write(strng)
