import os
from subprocess import getoutput,getstatusoutput

prg='./jump.py'

def test_exist():
    assert os.path.isfile(prg)

def test_usage():
    for arg in ['-h','--help']:
        rv,out=getstatusoutput(f'{prg} {arg}')
        assert rv==0
        assert out.lower().startswith('usage')

def test_encode_num():
    arg='123'
    out=getoutput(f'{prg} {arg}')
    expected='987'
    assert out.strip()==expected

def test_encode_txt():
    arg='abc123'
    out=getoutput(f'{prg} {arg}')
    expected='abc987'
    assert out.strip()==expected

