"""
hash (#) boarder around terminal
Nova -1fabunicorn
"""

from mainmodules import TermUtil

# loops through y axis in terminal. Note, you won't see the top hashes if ran by itself, as
# in the main game loop, the prompt won't be there

def border():
    xaxis, yaxis = TermUtil.get_terminal_size()[0], TermUtil.get_terminal_size()[1],
    for y in range(1, yaxis-1):

        if y == 1: # if on the first line
            print '#' * xaxis
        if y == yaxis-2: # and... if on the last line
            print '#' * xaxis

        else:  # prints side hashes if not the first or last
            print '#' + ' ' * (xaxis-2) + '#'
