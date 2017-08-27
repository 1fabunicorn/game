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


if __name__ == '__main__':
    HelloWorld().cmdloop()