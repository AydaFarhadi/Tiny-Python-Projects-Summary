import os
import sys
from subprocess import getoutput,getstatusoutput

prg="./crowsnest.py"

#lets pick some random words that are constant
consonant_words=[
    'brigantine','clipper','dreadnought','frigrate','junk','ketch',
    'longboat','vessel','whale','zebrafish'
]
#lets pick some random words that are vowel
vowel_words=['aviso','eel','iceberg']
template='Ahoy, Captain, {} {} off the larboard bow!'

#First test is always about the existance of the main file
def test_exists():
    """ file exists"""
    assert os.path.isfile(prg)
    
#Second test is about helpers. if user adds argumnet of h,help , the should see explanation about the program args 
def test_usage():
    """usage"""
    for flag in ['-h','--help']:
        rv,out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')    
        
#The rest of tests are about the functionality of program. Here we make sure if program receives constant, output will have a
def test_consonant():
    """ brigantine -> a brigantine """
    for word in consonant_words:
        out=getoutput(f'{prg} {word}')
        assert out.strip()==template.format('a',word)
        
#Here we make sure if program returns input revised such that first letter is uppercase
def test_consonanat_upper():
    """ brigantine -> a Brigrantine"""
    for word in consonant_words:
        out=getoutput(f'{prg} {word.title()}')
        assert out.strip()==template.format('a',word.title())
        
#Here we make sure if program receives vowel, output will have an
def test_vowels():
    for word in vowel_words:
        out=getoutput(f'{prg} {word}')
        assert out.strip()==template.format('an',word)
