import cmd
import subprocess
import os
import sys
from shlex import split


class HelloWorld(cmd.Cmd):

    prompt = os.getcwd() + '$ '

    def do_greet(self, person):
        '''
        greet [person]
        Greet the named person
        '''
        if person:
            print 'hi ' + person
        else:
            print 'hi'

    def do_EOF(self,nothing):
        print
        return True

    """
builtins
    """


    def do_cd(self, directory): #change directory
        '''
        syntax 'cd [directory]'
        change to [directory]
        '''
        args = directory.split(' ')
        try:
            os.chdir(args[0])

        except OSError:
            print 'not a directory'

        prompt = os.getcwd() + '$ '
        print os.getcwd()

    def do_pwd(self, nothing):
        '''
        syntax 'pwd'
        print working directory
        '''
        subprocess.check_call('pwd')

    def do_tree(self,line): # make a
        pass

    def do_cat(self, file):
        try:
            subprocess.check_call(['cat', file])
            print

        except KeyboardInterrupt:
            raise
        except:
            raise


if __name__ == 'mainmodules.CommandPrompt': # it works with this!!!
    HelloWorld().cmdloop()
