#!/usr/bin/env python3

import argparse

parser = argparser.ArgumentParser(description = 'Say hello')
parser.add_argument('name', help = 'Name to greet')
args = parser.parse_args()
print(args)
print("Hello, World!")