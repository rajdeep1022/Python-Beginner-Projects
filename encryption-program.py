# Python Encryption Program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#ENCRYPT
plaintext = input("Enter a message to encrypt: ")
ciphertext = ""

for letter in plaintext:
    index = chars.index(letter)
    ciphertext += key[index]

print(f"Original Message: {plaintext}")
print(f"Encrypted Message: {ciphertext}")

#DECRYPT
ciphertext = input("Enter a message to encrypt: ")
plaintext = ""

for letter in ciphertext:
    index = key.index(letter)
    plaintext += chars[index]

print(f"Encrypted Message: {ciphertext}")
print(f"Original Message: {plaintext}")
