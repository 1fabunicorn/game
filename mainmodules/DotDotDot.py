"""
    DotDotDot function
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

import time
import sys
import random

def uniformdots(loops, dots, timeper):
    for i in range(loops):
        print(dots * i)
        sys.stdout.write("\033[F")  # Cursor up one line
        time.sleep(timeper)


def ubscuredots(loops, texts):  # if this function is used more, I will make uniform dynamic
    for i in range(loops):
        sys.stdout.flush()
        sys.stdout.write(texts + ("." * i) + "\r")
        time.sleep(random.uniform(.05, .55))
    sys.stdout.write("\n")