"""
vigenere cipher
"""


def encrypt(plaintext, key):
    cyphertext = []

    for keyindex, plaintext in enumerate(plaintext):
        cyphertext.append( ord(plaintext) + ord(key[keyindex]) % (len(key)-1) % 256)
    return cyphertext


def decrypt(numbers, key):
    plaintext = []

    for keyindex, cyphertext in enumerate(numbers):
        plaintext.append(chr(cyphertext - (ord(key[keyindex])) % (len(key) - 1) % 256))
    return plaintext


print(encrypt("abc", 'dasdas'))
print(decrypt([97, 100, 99], 'dasdas'))