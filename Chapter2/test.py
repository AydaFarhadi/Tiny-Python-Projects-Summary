import os
import sys
from subprocess import getoutput,getstatusoutput

prg="./crowsnest.py"

consonant_words=[
    'brigantine','clipper','dreadnought','frigrate','junk','ketch',
    'longboat','vessel','whale','zebrafish'
]

vowel_words=['aviso','eel','iceberg']
template='Ahoy, Captain, {} {} off the larboard bow!'

def test_exists():
    """ file exists"""
    assert os.path.isfile(prg)

def test_usage():
    """usage"""
    for flag in ['-h','--help']:
        rv,out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')    

# def test_consonant():
#     """ brigantine -> a brigantine """
#     for word in consonant_words:
#         out=getoutput(f'{prg} {word}')
#         assert out.strip()==template.format('a',word)

# def test_consonanat_upper():
#     """ brigantine -> a Brigrantine"""
#     for word in consonant_words:
#         out=getoutput(f'{prg} {word.title()}')
#         assert out.strip()==template.format('a',word.title())

# def test_vowels():
#     for word in vowel_words:
#         out=getoutput(f'{prg} {word}')
#         assert out.strip()==template.format('an',word)