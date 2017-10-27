# -*- coding: utf-8 -*-
from __future__ import print_function
"""
    Input Output function
    reads from saves, writes plaintext on 'unlock'
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
from mainmodules import ignorethis


def write_plaintext(cyphertext, key, file_to_create):
    with open(cyphertext, 'r') as cyphertext_file:
        cyphertext_file = cyphertext_file.readlines(0)
    for x in cyphertext_file:
        cyphertext_file = x
    cyphertext_file = cyphertext_file.split()
    cyphertext_num = []
    for num in cyphertext_file:
        cyphertext_num.append(int(num))
    plaintext = ignorethis.decrypt(cyphertext_num, key)
    with open(file_to_create, 'w+') as f:
        print(plaintext, file=f)

def print_intro():
    spaces, bars, under_scores, new_lines = " ", "▇", "_", "\n"
    print((115 * bars) + (new_lines) + (2 * spaces) + (3 * bars) + (6 * spaces) +
          under_scores + (7 * spaces) + (2 * under_scores) + (spaces * 5) + (2 *
          under_scores) + (29 * spaces) + (6 * under_scores) + (48 * spaces) +
          (3 * bars) + new_lines + (2 * spaces) + (3 * bars) + (5 * spaces)
          + '| |     / /__  / /________  ____ ___  ___     /_  __/___' + (45 * spaces)
          + '▇▇▇\n  ▇▇▇     | | /| / / _ \\/ / ___/ __ \\/ __ `__ \\/ _ \\     '
            '/ / / __ \\        ____  ___________ _   _______  __   ▇▇▇\n  ▇▇▇     '
            '| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/    / / / /_/ /       / __ \\/'
            ' ____/ ___// | / /  _/ |/ /   ▇▇▇\n  ▇▇▇     |__/|__/\\___/_/\\'
            '___/\\____/_/ /_/ /_/\\___/    /_/  \\____/       / /_/ / __/  \\__ '
            '\\/  |/ // / |   /    ▇▇▇\n  ▇▇▇' + (35 * spaces) + '_'
          + (30 * spaces) + ' / _, _/ /___ ___/ / /|  // / /   |     ▇▇▇\n'
          '  ▇▇▇          _|_   _  _  |_  _ |._  _|__  _ |_  _ | _           '
          '     /_/ |_/_____//____/_/ |_/___//_/|_|     ▇▇▇\n  ▇▇▇        '
          '   |_\\/|_)(/_ | |(/_||_)  |(_)|  | |(/_||_)' + (55 * spaces)
          + '▇▇▇\n  ▇▇▇             / |             |                  |'
          + (57 * spaces) + '▇▇▇\n  ▇▇▇' + (106 * spaces) + (3 * bars)
          + (new_lines) + (2 * spaces) + (3 * bars) + (106 * spaces) + (3 * bars)
          + (new_lines) + (115 * bars))

def pw():
    try:
        password = raw_input("password: ")
    except NameError:
        input("password:")
    if password:
        return password
    else:
        return None
