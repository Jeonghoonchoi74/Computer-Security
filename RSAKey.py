import hashlib
from hashlib import sha512
from Crypto.PublicKey import RSA

def fast_modular_exponentiation(a,b,n):
    result = 1
    while b>0:
        if b%2 == 1:
          result = (result * a) % n
        a = (a * a) % n
        b //= 2
    return result

def rsa_signature_generation(message, d, n):
  digest = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
  signature = fast_modular_exponentiation(digest, d, n)
  return signature

def rsa_signature_verification(message, e, n, signature):
  digest = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
  verification = fast_modular_exponentiation(signature, e, n ) == digest
  return verification

print("RSA key generation")
keyPair = RSA.generate(bits = 1024)
print(" n = ", keyPair.n)
print(" e = ", keyPair.e)
print("d = ", keyPair.d)

t = input("message : ")
msg = bytes(t, 'utf-8')

signature = rsa_signature_generation(msg, keyPair.d, keyPair.n)
print("signature : ", signature)

verification = rsa_signature_verification(msg, keyPair.e, keyPair.n, signature)
print("확인결과 : ", verification)