"""
    dot dot dots (...)
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

import sys
import time


# loops = how many times it loops, message = the message it says, dots = what prints each loops, timeper = time per loop
def dot(loops, message, dots, timeper):
    for i in range(loops):
        print(message + dots * i)
        sys.stdout.write("\033[F")  # Cursor up one line
        time.sleep(timeper)
