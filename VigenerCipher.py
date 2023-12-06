#vigener cipher
def vigener(message, key):
    message = message.lower()
    message = message.replace (' ', '')
    m = len(key)
    cipher_text = ''
    for i in range (len(message)):
        letter = message[i]
        k = key[i%m]
        cipher_text = cipher_text + chr ((ord(letter)-97 + k)%26 + 97)

    return cipher_text

msg = input("plaintext : ")
key = input("key : ")
print(1)

key = [ord(letter)-97 for letter in key]
ciphertext = vigener(msg,key)
print('cipher text: ',ciphertext)

key = [-1*k for k in key]
plaintext = vigener(ciphertext, key)
print('Plain text : ', plaintext)