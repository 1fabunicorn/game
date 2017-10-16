"""
    cmd module class
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
import os
from mainmodules import cmdcopy, ignorethis, tasks, mail, datastruct
import subprocess
import time

d = datastruct.data


class HelloWorld(cmdcopy.Cmd):

    if not os.path.split(os.getcwd())[1] == 'user':
        os.chdir('user')  # changes directory to 'user'


    def do_EOF(self, line):
        '''
        syntax 'EOF'
        exit the game

        '''
        ignorethis.write_progress(str(d.progress))
        sys.exit('bye!\n')

    # ported builtins

    def do_cd(self, directory):  # change directory
        '''
        syntax 'cd [directory]'
        change to [directory]

        '''

        args = directory.split(' ')
        # next 6 lines are cheater proofing

        if args[0] == 'resnix':
            self.stdout.write('\nnot a directory\n')
            return

        if os.path.split(os.getcwd())[1] == '58.53.146.123' and args[0] == '..': # task 1 server
            self.stdout.write('\nnot a directory\n')
            return

        elif os.path.split(os.getcwd())[1] == 'user' and args[0] == '..':
            self.stdout.write('\nnot a directory\n')
            return

        try:
            os.chdir(args[0])
        except OSError:
            self.stdout.write('\nnot a directory\n')

    def do_pwd(self, nothing):
        '''
        syntax 'pwd'
        self.stdout.write working directory

        '''
        subprocess.check_call('pwd')

    def do_tree(self, nothing):
        '''
        syntax 'tree'
        print the directory structure as a tree

        '''
        # credit to dhobbs
        # https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/9728478#9728478

        startpath = os.getcwd()
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 2 * (level)
            self.stdout.write('{}{}/'.format(indent, os.path.basename(root)))
            self.stdout.write('\n')
            subindent = ' ' * 2 * (level + 1)
            for f in files:
                self.stdout.write('{}{}'.format(subindent, f))
                self.stdout.write('\n')

    def do_ls(self, args):
        '''
        syntax 'ls [optional args]'
        list files and directory's.
        If no args are specified, ls will self.stdout.write in alphabetical order
        for extended help, specify --help

        optional args

            -a  --all
              do not ignore entries starting with .
            -b  --escape
              self.stdout.write C-style escapes for nongraphic characters
            -h  --human-readable
              with -l and/or -s, self.stdout.write human readable sizes (e.g., 1K, 234M, 2G)
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
                self.stdout.write(data)
                self.stdout.write('\n')

        else:

            subprocess.check_call(['ls', args])

    def do_cat(self, file):
        '''
        syntax 'cat [file_to_cat]'

        cat - self.stdout.write files on the standard output
        for extended help, specify --help

        optional args

        -n, --number
          number all output lines
        -E, --show-ends
          display $ at end of each line

        '''

        subprocess.call(['cat', file])


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
            self.stdout.write('not a directory')
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
            self.stdout.write('not a directory')
            return
        elif not file:
            osCommandString = "vi " + "temp.txt"
        else:
            osCommandString = "vi " + file
        os.system(osCommandString)

    def do_vim(self, file):
        '''
        syntax 'nano [file_to_edit_or_create]'
        vi - a less friendly text editor


        if [file] is omitted, a temporary file will be created

        '''
        # hacker proofing
        if os.path.split(os.getcwd())[1] != os.path.split(file)[0] and file[0] == '/':
            self.stdout.write('not a directory')
            return
        elif not file:
            osCommandString = "vi " + "temp.txt"
        else:
            osCommandString = "vi " + file
        os.system(osCommandString)

    def do_touch(self, f):
        '''
        touch - "touch" or create a new file
        if file already exist, add an updated timestamp

        '''
        try:
            subprocess.call(['touch', f])
        except:
            self.stdout.write("file not specified")
    # ssh related functions

    def do_ssh(self, address):
        if address == '58.53.146.123':
            self.stdout.write("logging into 58.53.146.123")
            time.sleep(1)
            self.stdout.write("  ...success!\n")
            os.chdir('../dynamics/servers/58.53.146.123')
            d.login_count += 1

    def do_logout(self, none):
        if d.login_count > 1:
            for x in range(1,4):
                self.stdout.write("logging out " + ('.' * x) + "\r")
                time.sleep(0.25)
            self.stdout.write("\n")
            os.chdir('../../../user')
            d.login_count -= 1

        elif d.login_count == 1:
            self.do_EOF(None)

    # Game related stuff

    def do_browser(self,  webaddress):
        if webaddress.lower() == 'helloworld.net':
            os.system("lynx ../dynamics/htmls/helloworld.net.html")

    def do_progress(self, none):
        print(d.progress)
        # print(int(ignorethis.read_progress()))

    def do_unlock(self, key):
        '''
        unlock next task!
        syntax: unlock

        '''
        if key:
            try:
                ignorethis.write_plaintext(cyphertext=d.encrypted_files[d.progress], file_to_create=d.texts[d.progress], key=key)
            except KeyError:
                self.stdout.write("ds%^qWRONG3tgd%^KEY]\n")
        else:
            self.stdout.write("Please specify key\n")

    def do_mail(self, data):  # mail function
        '''
        email a person!
        syntax: mail [person@domain.net] [email body]

        '''

        d.progress = mail.mail_checkers(progress=d.progress, data=data)

    def do_leak(self, file):
        pass

    def do_meter(self, none):
        pass

    def do_check(self, data):
        '''
        help the user out if confused.
        ** work in progress **

        '''

        d.progress = tasks.task(d.progress)
        self.stdout.write('\nyou are at the %s stage.' % (d.num_to_words[d.progress]))
        self.stdout.write('\nrefer to "%s" for help on your task\n' % (d.texts[d.progress]))


if __name__ == 'mainmodules.CommandPrompt':
    HelloWorld()