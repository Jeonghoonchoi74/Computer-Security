P=7
Q=3
a=4
b=4


#Begin
print("공개 값들 : ")
print("       P  : ", P)
print("       Q  : ", Q)

#Alice Sends Bob A = g^a mod p
A = (Q ** a)%P
print("\nAllice sends : ", A)

#Bob Sends Alice B = g^b mod p
B = (Q ** b) % P
print("Bob sends : ", B)

print("\n----------------------\n")
print("비밀 키 계산")
#Alice Computes Shared Secret : s = B^a mod p
aliceSharedSecret = (B ** a) % P
print("       Alice 꺼 : ", aliceSharedSecret)

#Bob Computes Shared Secret : s = A^a mod p
bobSharedSecret = (A ** b ) % P
print("         Bob 꺼 : ", bobSharedSecret)
