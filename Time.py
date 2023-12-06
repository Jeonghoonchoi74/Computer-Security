from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

# RSA 키 쌍 생성 시간 측정
start_time = time.time()
keyPair = RSA.generate(2048)
end_time = time.time()
print(f"Key generation time: {end_time - start_time} seconds")

print("public key generating...")
pubKey = keyPair.publickey()
print(f" n = {hex(pubKey.n)}")
print(f" e = {hex(pubKey.e)}")

print("private key generating...")
print(f" d = {hex(keyPair.d)}")

msg = input("plaintext: ")
plaintext = bytes(msg, 'utf-8')

# 암호화 시간 측정
start_time = time.time()
encryptor = PKCS1_OAEP.new(pubKey)
ciphertext = encryptor.encrypt(plaintext)
end_time = time.time()

# 복호화 시간 측정
start_time = time.time()
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(ciphertext)
end_time = time.time()

# 총 소요 시간 출력
total_time = end_time - start_time
print(f"Total time: {total_time} seconds")
print("Cipher text:", binascii.hexlify(ciphertext))
print("Original text:", decrypted)
