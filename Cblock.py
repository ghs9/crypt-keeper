from Crypto.Cipher import AES
import requests


# mode = AES.MODE_CBC
# encryptor = AES.new(key, mode, IV=IV)
#
# text = 'j' * 64 + 'i' * 128
# ciphertext = encryptor.encrypt(text)





if __name__ == '__main__':

    key = '0123456789abcdef'
    IV = 16 * '\x00'           # placeholder

    r = requests.get('http://www.gutenberg.org/files/10/10-h/10-h.htm')
    print 'file loaded'

    string_words = r.text.split()
    print string_words
