#affine cipher
#E(x) = (ax + b) mod m
#m: size of the alphabet
#(a,b): keys of the cipher

def egcd(a,b):
    x,y, u,v = 0,1, 1,0
    while a!=0:
        q,r = b//a, b%a
        m,n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd !=1:
        return None
    else:
        return x%m

def encrypt(text, key):
    return ''.join([ chr(((key[0]*(ord(t) - ord('A'))+key[1])%26)+ord('A'))for t in text.upper().replace(' ','')])
def decrypt(cipher, key):
    return ''.join([ chr(((modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))%26)+ord('A'))for c in cipher])

msg = input("plaintext : ")
key = [7, 20]
enc_text= encrypt(msg,key)
print('ciphertext : {}'.format(enc_text))
print('decrypted text : {}'.format(decrypt(enc_text,key)))