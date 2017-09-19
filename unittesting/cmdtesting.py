import pytest
import sys
import os
try:
    sys.path.insert(0, os.path.split(os.getcwd())[0])
    from mainmodules import CommandPrompt
except Exception:
    from . import *
import random, string
"""
CommandPrompt tests:
tree function seems trivial, no seemingly good way to test it
"""


def randomstr(n):

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))


def test_cd(capsys):

    CommandPrompt.HelloWorld().do_cd('foo')
    out, err = capsys.readouterr()
    assert out == '\nnot a directory\n'
    assert err == ''

    CommandPrompt.HelloWorld().do_cd('texts')
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''

    CommandPrompt.HelloWorld().do_cd(randomstr(10))
    out, err = capsys.readouterr()
    assert out == '\nnot a directory\n'
    assert err == ''

def test_EOF():
    pass


def test_pwd():
    pass

def test_ls():
    pass

def test_cat():
    pass

def test_check():
    pass

def test_touch():
    pass

