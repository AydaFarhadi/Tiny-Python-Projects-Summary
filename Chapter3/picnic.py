
#
#!/usr/bin/env python3
"""
Author : alireza <alireza@localhost>
Date   : 2023-02-10
Purpose:Print item on picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        type = str,
                        nargs ='+', ### Here we can acept more than one argument
                        help='Items we are bringing')


    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():  ## This is the main function where the program wil start.
    """Make a jazz noise here"""

    args = get_args() 
    # We are calling this function and putting the returned 
    # value into  the variable args.

    items = args.item
    # We copy items into a new variable items
    print(args.item)
    print(args.sorted)
    # print(items.sort())

    bringing = '' 
    # Using an empty string to initilize a variable to hold 
    # the items we are brining

    if args.sorted:
        items.sort()


    if len(items) == 1:
        bringing = items[0]
   #     print('You are bringing ' + items[0] + '.')
    elif len(items) == 2:
        bringing =' and '.join(items)
  #      print('You are bringing ' + items[0] + ' and '+ items[1] +'.')
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)
      #  print('You are bringing {}.'.format(bringing))

    print('You are bringing {}.'.format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
# When Python runs the program, it will read all the 
# lines to this point but will not run anything. 
# Here we look to see if we are in
# the “main” namespace. If we are, we call the main() 
# function to make the program begin