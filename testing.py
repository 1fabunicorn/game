"""
from mainmodules import ignorethis
import pickle
welcome = "Welcome. We don't have much time. I hear you love the open source. Lets keep it this way.\nthree hours ago, the linux kernel was made illegal. We, the opposition feel they have something they don't want us to know.\nPlease, first host linux kernel 0.1 on your public ftp server. We have a script to make it safe, not to compromise your identity\n\n\n(sudo script here)\n\ngod speed"

cyphertext = ignorethis.encrypt(welcome,'resist')
# print(cyphertext)

# print ignorethis.decrypt([201, 202, 223, 204, 226, 225, 215, 147, 147, 192, 216, 148, 214, 212, 225, 144, 231, 148, 218, 198, 233, 206, 147, 225, 231, 200, 219, 137, 231, 221, 223, 202, 161, 137, 188, 148, 218, 202, 212, 219, 147, 237, 225, 218, 147, 213, 226, 234, 215, 133, 231, 209, 216, 148, 225, 213, 216, 215, 147, 231, 225, 218, 229, 204, 216, 162, 146, 177, 216, 221, 230, 148, 221, 202, 216, 217, 147, 221, 230, 133, 231, 209, 220, 231, 146, 220, 212, 226, 161, 126, 230, 205, 229, 206, 216, 148, 218, 212, 232, 219, 230, 148, 211, 204, 226, 149, 147, 232, 218, 202, 147, 213, 220, 226, 231, 221, 147, 212, 216, 230, 224, 202, 223, 137, 234, 213, 229, 133, 224, 202, 215, 217, 146, 206, 223, 213, 216, 219, 211, 209, 161, 137, 202, 217, 158, 133, 231, 209, 216, 148, 225, 213, 227, 216, 230, 221, 230, 206, 226, 215, 147, 218, 215, 202, 223, 137, 231, 220, 215, 222, 147, 209, 212, 234, 215, 133, 230, 216, 224, 217, 230, 205, 220, 215, 218, 148, 230, 205, 216, 226, 147, 216, 225, 211, 154, 221, 147, 235, 211, 211, 231, 137, 232, 231, 146, 217, 226, 137, 222, 226, 225, 220, 161, 115, 195, 224, 215, 198, 230, 206, 159, 148, 216, 206, 229, 220, 231, 148, 218, 212, 230, 221, 147, 224, 219, 211, 232, 225, 147, 223, 215, 215, 225, 206, 223, 148, 162, 147, 164, 137, 226, 226, 146, 222, 226, 222, 229, 148, 226, 218, 213, 213, 220, 215, 146, 203, 231, 217, 147, 231, 215, 215, 233, 206, 229, 162, 146, 188, 216, 137, 219, 213, 232, 202, 147, 202, 147, 231, 213, 215, 220, 217, 231, 148, 230, 212, 147, 214, 212, 223, 215, 133, 220, 221, 147, 231, 211, 203, 216, 149, 147, 226, 225, 217, 147, 221, 226, 148, 213, 212, 224, 217, 229, 227, 223, 206, 230, 206, 147, 237, 225, 218, 229, 137, 220, 216, 215, 211, 231, 210, 231, 237, 124, 111, 125, 145, 230, 233, 214, 212, 147, 220, 214, 230, 219, 213, 231, 137, 219, 217, 228, 202, 156, 115, 125, 219, 225, 201, 147, 220, 227, 217, 215, 201], 'resist')

ignorethis.write_plaintext('articles/welcome.encrypted.txt', key='resist', file_to_create='welcome.blob')
"""
import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


list_files('/Users/student/Desktop/dev/game/user')