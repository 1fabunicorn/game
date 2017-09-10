"""
hash (#) boarder around terminal
Nova Trauben -1fabunicorn
loops through y axis in terminal. Note, you won't see the top hashes if ran by itself, as
in the main game loop, the prompt won't be there

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
