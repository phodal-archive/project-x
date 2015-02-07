import getpass
import sys
import twill


try:
    import pkg_resources
except ImportError:
    raise Exception("you must have setuptools installed to run the tests")

from cStringIO import StringIO
import os

testdir = os.path.dirname(__file__)
print 'testdir is:', testdir
sys.path.insert(0, os.path.abspath(os.path.join(testdir, '..')))


def execute_twill_script(filename, inp=None, initial_url=None):
    global testdir

    if inp:
        def new_getpass(*args):
            return ""

        inp_fp = StringIO(inp)
        old, sys.stdin = sys.stdin, inp_fp
        old_getpass, getpass.getpass = getpass.getpass, new_getpass

    scriptfile = os.path.join(testdir, filename)
    try:
        twill.execute_file(filename, initial_url=initial_url)
    finally:
        if inp:
            sys.stdin = old
            getpass.getpass = old_getpass


def execute_twill_shell(filename, inp=None, initial_url=None,
                        fail_on_unknown=False):
    # use filename as the stdin *for the shell object only*
    scriptfile = os.path.join(testdir, filename)
    
    cmd_inp = open(scriptfile).read()
    cmd_inp += '\nquit\n'
    cmd_inp = StringIO(cmd_inp)

    # use inp as the std input for the actual script commands.
    if inp:
        inp_fp = StringIO(inp)
        old, sys.stdin = sys.stdin, inp_fp

    try:
        try:
            s = twill.shell.TwillCommandLoop(initial_url=initial_url,
                                             stdin=cmd_inp,
                                             fail_on_unknown=fail_on_unknown)
            s.cmdloop()
        except SystemExit:
            pass
    finally:
        if inp:
            sys.stdin = old
    