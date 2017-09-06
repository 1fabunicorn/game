# import mainmodules.CommandPrompt
import string
backward = {}
forward = {}

for counter, char in enumerate(string.printable):  # backward
    backward[counter] = char

for counter, char in enumerate(string.printable): # forward
    forward[char] = counter


print(backward)
print(forward)
