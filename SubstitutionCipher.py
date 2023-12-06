#Substitution cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "fcpevqkzgmtrayonujdlwhbxsi"

def encrypt(text, key):
    result = ""
    for letter in text:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter
    return(result)

msg = input("plaintext: ")
print(encrypt(msg, key))