"""
vigenere cipher
"""


def encrypt(plaintext, key):
    cyphertext = []
    len_of_key = len(key)

    for keyindex, plaintext in enumerate(plaintext):
        cyphertext.append(ord(plaintext) + ord(key[keyindex % len_of_key]) % 255)
    return cyphertext


def decrypt(cyphertext, key):
    plaintext = []
    len_of_key = len(key)

    for keyindex, numbers in enumerate(cyphertext):
        plaintext.append(chr(numbers - ord(key[keyindex % len_of_key]) % 255))
    return plaintext
