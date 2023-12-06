import random
from math import pow
import time

# 최대공약수를 계산하는 함수
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 큰 난수 생성
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key

# 거듭제곱을 계산
def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

# 암호화
def encrypt(msg, q, h, g):
    en_msg = []
    k = gen_key(q)  # 발신자의 개인 키
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
    print("g^k used:", p)
    print("g^ak used:", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
    return en_msg, p

# 복호화
def decrypt(en_msg, p, key, q):
    dr_msg = []
    hh = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / hh)))
    return dr_msg

msg = input("plaintext: ")
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)  # 수신자의 개인 키
h = power(g, key, q)
print("g used:", g)
print("g^a used:", h)

# 암호화 및 복호화 작업 전후의 시간 측정
start_time = time.time()
en_msg, p = encrypt(msg, q, h, g)
dr_msg = decrypt(en_msg, p, key, q)
end_time = time.time()

print(end_time - start_time)
dmsg = ''.join(dr_msg)
print("Original text:", dmsg)
