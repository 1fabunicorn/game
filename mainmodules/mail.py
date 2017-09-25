"""
    mail module class
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

# The similarity's between this and checks is great, I may refactor in the future

import DotDotDot


def mail_checkers(data, progress):  # mail function

    data = data.split()
    if progress == -1:
        try:
            if data[0] == 'anon@resnix.net':

                print('welcome to the club')
                DotDotDot.dot(20, '.', .2)
                print('receiving data')
                DotDotDot.dot(14, '.', .2)
                print('Quick! Change line two of etc/ftp.comf to true')
                progress += 0
                return progress
        except KeyError:
            print('No email specified')

        print('\n')