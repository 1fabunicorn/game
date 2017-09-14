"""
    hash (#) boarder around terminal
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


from mainmodules import TermUtil


def border():
    x_axis, y_axis = TermUtil.get_terminal_size()[0], TermUtil.get_terminal_size()[1],
    for y in range(1, y_axis-1):

        if y == 1: # if on the first line
            print('#' * x_axis)
        if y == y_axis-2: # and... if on the last line
            print('#' * x_axis)

        else:  # prints side hashes if not the first or last
            print('#' + ' ' * (x_axis-2) + '#')
