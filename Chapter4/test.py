import os
from subprocess import getoutput,getstatusoutput

prg='./jump.py'

def test_exist():
    """
    1.Test is always about the existance of file 
    """
    assert os.path.isfile(prg)

def test_usage():
    """
    2.Test help to make sure when user uses h,help they will receive enough information about argument of program  
    """
    for arg in ['-h','--help']:
        rv,out=getstatusoutput(f'{prg} {arg}')
        assert rv==0
        assert out.lower().startswith('usage')

def test_encode_num():
    """
    Hard code an argument and test to make sure the output will look like what we are expecting form model to get on encoded side
    """
    arg='123'
    out=getoutput(f'{prg} {arg}')
    expected='987'
    assert out.strip()==expected

def test_encode_txt():
    """
    Add text at the end of it. This will make sure that only numbers will change not text
    """
    arg='abc123'
    out=getoutput(f'{prg} {arg}')
    expected='abc987'
    assert out.strip()==expected

