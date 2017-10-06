from __future__ import print_function
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
        if numbers > 255 or numbers < 0:
            raise ValueError

        plaintext.append(chr(numbers - ord(key[keyindex % len_of_key]) % 255))
    return "".join(plaintext)


def write_plaintext(cyphertext, key, file_to_create):
    with open(cyphertext, 'r') as cyphertext_file:
        cyphertext_file = cyphertext_file.readlines(0)
    for x in cyphertext_file:
        cyphertext_file = x
    cyphertext_file = cyphertext_file.split()
    cyphertext_num = []
    for num in cyphertext_file:
        cyphertext_num.append(int(num))
    plaintext = decrypt(cyphertext_num, key)
    with open(file_to_create, 'w+') as f:
        print(plaintext, file=f)


def read_progress():
    try:
        with open('../gamedata', 'r') as f:
            p = f.readlines()
        return ''.join(p)
    except IOError:
        p = -1
        return p


def write_progress(variable):
    with open('../gamedata', 'w+') as f:
        f.write(variable)
    return variable
