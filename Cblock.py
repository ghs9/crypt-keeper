if __name__ == '__main__':
    from Crypto.Cipher import AES
    key = '0123456789abcdef'
    IV = 16 * '\x00'           # placeholder
    mode = AES.MODE_CBC
    encryptor = AES.new(key, mode, IV=IV)

    import requests
    r = requests.get('http://www.gutenberg.org/files/10/10-h/10-h.htm')
    print 'file loaded'

    text = r.text
    chunk_size = 16
    block_array = [str(text[i:i+chunk_size]) for i in range(0, len(text), chunk_size)]

    #this shit give some strange ass text :()
    print IV + encryptor.encrypt("1234567890abcdef")
    
    # for block in block_array:
    #     ciphertext = encryptor.encrypt(block)
