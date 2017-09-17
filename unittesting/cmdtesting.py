import pytest
class testing():
    """
    CommandPrompt tests:
    tree function seems trivial, no seemingly good way to test it
    """

    def test_EOF(self):

        self.assertRaises(SystemExit, CommandPrompt.HelloWorld().do_EOF,'EOF')
        self.assertRaises(SystemExit, CommandPrompt.HelloWorld().do_EOF, None)

    def test_cd(self):
        self.assertEqual(CommandPrompt.HelloWorld().do_cd('foo'), '\nnot a directory')


    def test_pwd(self):
        pass

    def test_ls(self):
        pass

    def test_cat(self):
        pass

    def test_check(self):
        pass

    def test_touch(self):
        pass
