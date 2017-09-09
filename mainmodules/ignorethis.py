"""
Nova Trauben
vigenere cipher, as well as writing of cyphertext to file

Notes:
    It seems this function is relatively efficient, as timeit says,
    10000 loops, best of 3: 59.4 usec per loop
    returns a list of encrypted values, and plaintext values. Not sure where to go from their.
"""
import pickle

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
    return "".join(plaintext)


def write_plaintext(cyphertext, key, file_to_create):
    with open(cyphertext, 'rb') as file:
        encrypted = pickle.load(file)

    plaintext = decrypt(encrypted,key)

    with open(file_to_create, 'w') as f:
        f.write(plaintext)
