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
def task(progress, saves):

    if progress == -1:

        try:
            with open("etc/ftp.comf", "r") as f:
                line = f.readlines()
                if line[2] == 'online = true' or line[2] == 'online= true' or line[2] == 'online =true' or line[2] == 'online=true':
                    print(('#' * 55) + '\nNice job on your first task!\n  Unlock your next task with "unlock resist"\n' + ('#' * 55))
                    progress = 0
                    return progress
                else:
                    print('something is wrong....\n')
                    progress = -1
                    return progress
        except IOError:
            print('Run check from the root directory (user)')
            progress = -1
            return progress


    if progress == 0:
        try:

            with open("etc/ftp.comf", "r") as f:
                line = f.readlines()
                if line[1] == 'anon_access = true\n' or line[1] == 'anon_access= true\n' or line[1] == \
                        'anon_access =true\n' or line[1] == 'anon_access=true\n':
                    print(('#' * 55) + '\nNice job. What is the RFC for the FTP protocol version you are using now?\n  Try it out with "unlock [key]"\n'
                          + ('#' * 55))
                    progress = 1
                    return progress
                else:
                    print('something is wrong....\n')
                    progress = 0
                    return progress
        except IOError:
            print('Run check from the root directory (user)')
            progress = 0
            return progress


    if progress == 1:
        print(('#' * 55) + "\nWhat drives markets?\nTry it out with 'unlock [word]'")
        try:
            with open('/texts/AKAspy.blob', 'r') as f:
                if f.readlines()[0:4] == "Check":
                    # ask question here for unlock key
                    return progress
                else:
                    print('something is wrong....\n')
                    progress = 1
                    return progress

        except IOError:
            print('something is wrong, did you find the unlock key?\nPossibly the file, '
                  'AKAspy.blob doest exist?')

        progress = 2
        return progress


    if progress == 2:
        if saves["point_1"]["template.txt"] == 0 or saves["point_1"]["qwerty.txt"] == 0:
            print("You have some vital data you could leak!")
        else:
            progress += 1
        return progress


    if progress > 2:
        print("It seems you have reached the end of the game...")
        print("NOPE! I am still making it!")
        print("Stay tuned! :)")
        return progress
