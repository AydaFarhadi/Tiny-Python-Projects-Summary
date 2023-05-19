#!/usr/bin/env python3
### what is that?
"""tests for picnic.py"""
### what is that?

import os
### what is that?
from subprocess import getoutput
### what is that?

prg = './picnic.py'
### what is that? I know, this is the file ...

# --------------------------------------------------
def test_exists():
    """exists"""
    assert os.path.isfile(prg)


# --------------------------------------------------
# args
def test_usage():
    """usage"""
    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')
        # usage: picnic.py [-h] [-s] str [str ...]
        # This usage come  from this line  assert out.lower().startswith('usage')


# The strip() method returns a copy of the string by removing both 
# #the leading and the trailing characters (based on the string argument passed)
# --------------------------------------------------
def test_one():
    """one item"""
    args = 'chips'
    out = getoutput(f'{prg} {args}')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""
    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected
