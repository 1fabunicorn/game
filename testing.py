import cmd


class HelloWorld(cmd.Cmd):
    prompt = '$ '
    def do_greet(self, person):
        """
        greet [person]
        Greet the named person
        """
        if person:
            print 'hi ' + person
        else:
            print 'hi'

    def do_EOF(self, line):
        print
        return True
    def do_test(self, line):
        '''
        This is only a test
        '''
        print 'This is a test command.'


if __name__ == '__main__':
    HelloWorld().cmdloop()
