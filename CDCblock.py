from Crypto.Cipher import AES


key = "0123456789ABCDEF"
iv =  "0000000000009001"
plaintext = ""
with open('pg10.txt', 'r') as file:
    for line in file:
        plaintext += line

length = 16 - (len(plaintext) % 16)
plaintext += chr(length)*length

obj = AES.new('This is a key123', AES.MODE_CBC, iv)

ciphertext = obj.encrypt(plaintext)

file = open("encryptedCBC.txt", 'w+')
file.write(ciphertext)

obj2 = AES.new('This is a key123', AES.MODE_CBC, iv)

decr = obj2.decrypt(ciphertext)

decr = decr[:-(length)]

file = open("decryptedCBC.txt", 'w+')
file.write(decr)
