import cmdcopy
import subprocess
import os
from shlex import split
import tempfile


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

    def do_EOF(self,nothing):
        print()
        return True

    """
ported builtins
    """


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

    def do_tree(self,line): # make a
        pass

    def do_ls(self,args):


        try:
            subprocess.check_call(['ls', args])
        except:
            l = os.listdir(os.getcwd())
            for file in l:
                print(file)


    def do_cat(self, file):
        try:
            subprocess.check_call(['cat', file])
            print()
        except:
            raise

    def do_clear(self,line):
        print("\n"*15)

    def do_nano(self, file):
        osCommandString = "nano" + file
        os.system(osCommandString)

    def do_vi(self, file):
        osCommandString = "vi" + file
        os.system(osCommandString)

    def do_touch(self,file):
        subprocess.call(['touch', file])


if __name__ == 'mainmodules.CommandPrompt': # it works with this!!!
    HelloWorld().cmdloop()
