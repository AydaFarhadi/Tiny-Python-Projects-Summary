#!/usr/bin/env python3
"""
Author : aydafarhadi <aydafarhadi@localhost>
Date   : 2023-01-15
Purpose: Rock the Casbah
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word',
                        metavar='word',
                        help='things that we see')
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word=args.word
    article='an' if word[0].lower() in 'aeio' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
