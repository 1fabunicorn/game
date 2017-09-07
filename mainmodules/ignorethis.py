"""
Nova Trauben
vigenere cipher

Notes:
    It seems this function is relatively efficient, as timeit says,
    10000 loops, best of 3: 59.4 usec per loop
    returns a list of encrypted values, and plaintext values. Not sure where to go from their.
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
    return "".join(plaintext)


def write_plaintext(cyphertext, key, file_to_create, ):
    pass

    file = open(cyphertext, 'r')
    file_name = file.readline()
    file_name += ".txt"

    for words in cyphertext:
        file_to_create = open(file_to_create, 'a')
        file_to_create.write(decrypt(cyphertext, key))

    print(file_name)
