#https://en.wikipedia.org/wiki/RC4
#Pseuduoooo codeee
def KSA(key):
    keylength = len(key)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == '__main__':
    from Crypto.Hash import SHA384
    from Crypto import Random
    key = 'Key'
    nonce = Random.new().read(16)
    key = SHA384.new(key+nonce).digest()
    # plaintext = 'Plaintextaoeuoeuaoeu'

    import requests
    r = requests.get('http://www.gutenberg.org/files/10/10-h/10-h.htm')
    text = r.text

    def convert_key(s):
        return [ord(c) for c in s]

    key = convert_key(key)
    keystream = RC4(key)

    # print "file loaded"
    import sys
    encrypted = ""
    for char in r.text:
        encrypted += "%02X" % (ord(char) ^ keystream.next())
    # print encrypted
    file = open('RC4encrypted.txt', 'w+')
    file.write(encrypted)
