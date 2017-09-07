# import mainmodules.CommandPrompt
from mainmodules import ignorethis

print(ignorethis.encrypt("This is a test on how data will be written\n is this a new line?", 'password'))
print(ignorethis.decrypt([196, 201, 220, 230, 151, 216, 229, 132, 209, 129, 231, 216, 234, 227, 146, 211, 222, 129, 219, 226, 238, 143, 214, 197, 228, 194, 147, 234, 224, 219, 222, 132, 210, 198, 147, 234, 233, 216, 230, 216, 213, 207, 125, 147, 224, 226, 146, 216, 216, 202, 230, 147, 216, 143, 224, 201, 231, 129, 223, 220, 229, 212, 177]
, 'password'))