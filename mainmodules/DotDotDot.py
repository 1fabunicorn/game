import sys
import time


# loops = how many times it loops, message = the message it says, dots = what prints each loops, timeper = time per loop
def dot(loops, message, dots, timeper):
    for i in range(loops):
        print(message + dots * i)
        sys.stdout.write("\033[F")  # Cursor up one line
        time.sleep(timeper)
