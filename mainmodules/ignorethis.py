"""
    vigenere cipher, as well as writing of cyphertext to file
    Copyright (C) 2017,  Nova Trauben, noah.trauben@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""



import pickle


def encrypt(plaintext, key):
    """

    :param plaintext: unencrypted text
    :param key: encryption key
    :return: returns cyphertext
    """
    cyphertext = []
    len_of_key = len(key)

    for keyindex, plaintext in enumerate(plaintext):
        cyphertext.append(ord(plaintext) + ord(key[keyindex % len_of_key]) % 255)
    return cyphertext


def decrypt(cyphertext, key):
    """

    :param cyphertext: encrypted plaintext
    :param key: encryption key
    :return: return plaintext
    """
    plaintext = []
    len_of_key = len(key)

    for keyindex, numbers in enumerate(cyphertext):
        plaintext.append(chr(numbers - ord(key[keyindex % len_of_key]) % 255))
    return "".join(plaintext)


def write_plaintext(cyphertext, key, file_to_create):
    """

    :param cyphertext: file where cyphertext excists in a pickled form
    :param key: the decryption key
    :param file_to_create: file that is created. user/texts/ is appended to the front of the file
    :return: if directory doesnt exsist, return, otherwise, create file
    """

    try:
        with open(cyphertext, 'rb') as file:
            encrypted = pickle.load(file)

        plaintext = decrypt(encrypted,key)
        file_to_create = 'user/texts/' + file_to_create

        with open(file_to_create, 'w') as f:
            f.write(plaintext)
    except IOError:
        return "directory doesn't exist"
