import cmd
from shlex import split
# from https://pymotw.com/3/cmd/

class HelloWorld(cmd.Cmd):

    prompt = '$ '


    def do_greet(self, person):
        '''
        greet [person]
        Greet the named person
        '''
        if person:
            print 'hi ' + person
        else:
            print 'hi'

    def do_EOF(self, line):
        print
        return True

    def do_test(self, var1):
        '''
        This is only a test
        '''

        split = var1.split(' ')

        print 'var1: ' + split[0] + ' var2: ' + split[1]


if __name__ == 'mainmodules.CommandPrompt': # it works with this!!!
    HelloWorld().cmdloop()
