"""
    task module. Separated game logic checks
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


def task(progress):

    if progress == -1:
        with open("../user/etc/ftp.comf", "r") as f:
            line = f.readlines()
            if line[2] == 'online = true' or line[2] == 'online= true' or line[2] == 'online =true' or line[2] == 'online=true':
                print('Nice job on your first task!\n  Unlock your next task with "unlock resist"')
                progress = 0
                return progress
            else:
                print('something is wrong....\n')
                progress = -1
                return progress


    if progress == 0:
        with open("../user/etc/ftp.comf", "r") as f:
            line = f.readlines()
            if line[1] == 'anon_access = true\n' or line[1] == 'anon_access= true\n' or line[1] == \
                    'anon_access =true\n' or line[1] == 'anon_access=true\n':
                print(('#' * 55) + '\nNice job. What is the modern RFC for the FTP protocol?\n  Try it out with "unlock [key]"\n'
                      + ('#' * 55))
                progress = 1
                return progress
            else:
                print('something is wrong....\n')
                progress = 0
                return progress