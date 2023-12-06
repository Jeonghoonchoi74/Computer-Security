# 3DES
from Crypto.Cipher import DES3

key = b'1234567890abcdef' # 16 bytes
iv = b'12345678'
cipher1 = DES3.new(key, DES3.MODE_CFB, iv)

msg = input("plaintext : ")
plaintext = bytes(msg, 'utf-8')
ciphertext = cipher1.encrypt(plaintext)
print('ciphertext : ', ciphertext)

cipher2 = DES3.new(key, DES3.MODE_CFB, iv)
print("decrypting ... ", cipher2.decrypt(ciphertext))