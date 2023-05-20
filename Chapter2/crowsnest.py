#!/usr/bin/env python3
"""
Author : aydafarhadi <aydafarhadi@localhost>
Date   : 2023-01-15
Purpose: Rock the Casbah
"""
import argparse
# -------------------------------------------------
def get_args():
    """Get command-line arguments.
     ArgumentParser is a class of argparse module. 
     It has functions such as "add_argument" that receives arguments and metavar adds hint about that argument
    """
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word',
                        metavar='word',
                        help='things that we see')
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here.
    here we get arguments using the helper function that defined about (get_args).
    Then extract word from argument that we captures using that function
    Then check if first letter of that word is vowel, we use 'an' otherwise we use 'a'
    """
    args = get_args()
    word=args.word
    article='an' if word[0].lower() in 'aeio' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
    
# --------------------------------------------------
if __name__ == '__main__':
    """
    Most of the programs should have main method to run . 
    There could be a lot of helper function ,but suing main at the end of file could put them together and run it.
    """
    main()
