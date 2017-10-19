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
import ignorethis
import pickle


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


def read_lp_tracks():
    # lp_tracks = []
    # try:
    #     with open('../saves', 'r') as f:
    #         p = f.readlines()
    #     lst = [item for sublist in p for item in sublist]
    #     flat = "".join(lst)
    #
    #     lp_tracks.append(flat.split()[2])
    #     lp_tracks.append(flat.split()[3])
    #     lp_tracks.append(flat.split()[4])
    #     return lp_tracks
    # except IndexError:
    #     lp_tracks = ['FF', 'FFFF', 'FFFF']
    #     return lp_tracks
    # except IOError:
    #     lp_tracks = ['FF', 'FFFF', 'FFFF']
    #     return lp_tracks
    return pickle.load(open('../saves', 'r'))


def read_progress():
    try:
        with open('../saves', 'r') as f:
            p = f.readlines()
        lst = [item for sublist in p for item in sublist]
        flat = "".join(lst)
        return int(flat.split()[0])
    except IndexError:
        p = -1
        return p
    except IOError:
        p = -1
        return p


def read_leakpoints():
    try:
        with open('../saves', 'r') as f:
            p = f.readlines()
        lst = [item for sublist in p for item in sublist]
        flat = "".join(lst)
        return int(flat.split()[1])
    except IndexError:
        lp = 0
        return lp
    except IOError:
        lp = 0
        return lp


def write_progress(saves):
    # with open('../saves', 'w+') as f:
    #     f.write(progress)
    #     f.write(" ")
    #     f.write(leak_points)
    # return

    pickle.dump(saves, open("../saves", "wb"))


