import cmdcopy
import subprocess
import os
from shlex import split
import sys


class HelloWorld(cmdcopy.Cmd):
    os.chdir('user')  # changes directory to 'user'

    def do_greet(self, person):
        '''
        greet [person]
        Greet the named person
        '''
        if person:
            print('hi ' + person)
        else:
            print('hi')


    def do_EOF(self, line):
        '''
        syntax 'EOF'
        '''
        sys.exit('bye!')


#ported builtins


    def do_cd(self, directory): #change directory
        '''
        syntax 'cd [directory]'
        change to [directory]
        '''

        args = directory.split(' ')
        # next 6 lines are cheater proof biz
        if args[0] == 'game':
            print('not a directory')
            return
        if os.path.split(os.getcwd())[1] == 'user' and args[0] == '..':
            print('not a directory')
            return

        try:
            os.chdir(args[0])
        except OSError:
            print('not a directory')

    def do_pwd(self, nothing):
        '''
        syntax 'pwd'
        print working directory
        '''
        subprocess.check_call('pwd')

    def do_tree(self, nothing):
        '''
        syntax 'tree'
        prints the directory structure as a tree

        '''
        # credit to dhobbs
        # https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/9728478#9728478

        startpath = os.getcwd()
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    def do_ls(self, args):
        '''
        syntax 'ls [optional args]'
        list files and directory's.
        If no args are specified, ls will print in alphabetical order
        for extended help, specify --help

        optional args

            -a  --all
              do not ignore entries starting with .
            -b  --escape
              print C-style escapes for nongraphic characters
            -h  --human-readable
              with -l and/or -s, print human readable sizes (e.g., 1K, 234M, 2G)
            -I  --ignore=PATTERN
              do not list implied entries matching shell PATTERN
            -l
              use a long listing format
            -1
              list one file per line.  Avoid '\n' with -q or -b
        '''

        if not args:
            listdir = os.listdir(os.getcwd())
            for data in listdir:
                print(data)
        else:

            subprocess.check_call(['ls', args])


    def do_cat(self, file):
        '''
        syntax 'cat [file_to_cat]'

        cat - print files on the standard output
        for extended help, specify --help

        optional args

        -n, --number
          number all output lines
        -E, --show-ends
          display $ at end of each line
        '''

        try:
            subprocess.check_call(['cat', file])
        except:
            pass

    def do_clear(self, nothing):
        '''
        clear - clear the terminal screen

        '''

        subprocess.call(['clear'])

    def do_nano(self, file):
        '''
        syntax 'nano [file_to_edit_or_create]'
        nano - friendly text editor

        if [file] is omitted, a temporary file will be created

        '''
        # hacker proofing
        if os.path.split(os.getcwd())[1] != os.path.split(file)[0] and file[0] == '/':
            print('not a directory')
            return

        elif not file:
            osCommandString = "nano " + "temp.txt"

        else:
            osCommandString = "nano " + file

        os.system(osCommandString)

    def do_vi(self, file):
        '''
        syntax 'nano [file_to_edit_or_create]'
        vi - a less friendly text editor


        if [file] is omitted, a temporary file will be created

        '''

        # hacker proofing
        if os.path.split(os.getcwd())[1] != os.path.split(file)[0] and file[0] == '/':
            print('not a directory')
            return
        elif not file:
            osCommandString = "vi " + "temp.txt"
        else:
            osCommandString = "vi " + file
        os.system(osCommandString)

    def do_touch(self, file):
        '''
        touch - "touch" or create a new file
        if file already exist, add an updated timestamp

        '''
        try:
            subprocess.call(['touch', file])
        except:
            print("file not specified")


if __name__ == 'mainmodules.CommandPrompt': # it works with this!!!
    HelloWorld().cmdloop()
