#shift cipher
def encrypt(text,key):
    result=""
    #transverse the plain text
    for i in range (len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + key-65)%26 + 65)
        else:
            result += chr((ord(char)+ key-97)%26 + 97)
    return result
msg = input("plaintext : ")
key = input ("key : ")

ciphertext = encrypt(msg, int(key))
print(ciphertext)

#이거는 Sense test
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
for key in range (len(LETTERS)):
    translated = ''
    for symbol in ciphertext:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num-key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated+ LETTERS[num]
        else:
            translated = translated + symbol
    print('Hacking key #%s : %s' % (key, translated))