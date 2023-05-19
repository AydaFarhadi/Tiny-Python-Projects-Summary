#!/usr/bin/env python3  
#--> The shebang line tells the operating system to  use /usr/bin/env 
# ---->to find python3 to interpret this program.


#---> A comment line documenting the purpose of the program
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput


prg = './hello.py'
# here . dot means the current working directory
#  and slash / means is how we seperate eah directory
#  from each other


# The first test always checks that the expected file exists. Here the test looks for hello.py.
# --------------------------------------------------
def test_exists():
    """exists"""
    assert os.path.isfile(prg)


    # The second test tries to run the program with python3 hello.py and then checks if the program printed “Hello, World!” If you miss even one character, like forgetting a comma, the test will point out the error, so read carefully!

# --------------------------------------------------
def test_runnable():
    """Runs using python3"""
    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'


    # The third test checks that the program is “executable.” This test fails, so next we’ll talk about how to make that pass.
# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""
    out = getoutput(prg)
    assert out.strip() == 'Hello, World!'


    # The fourth test asks the program for help and doesn’t get anything. We’re going to add the ability to print a “usage” statement that describes how to use our program.

# --------------------------------------------------
def test_usage():
    """usage"""
    
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


        # The last test checks that the program can greet a name that we’ll pass as an argument. Since our program doesn’t yet accept arguments, we’ll need to add that, too.
# --------------------------------------------------
#9-
def test_input():
    """test for input"""
    
    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
