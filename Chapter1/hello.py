#!/usr/bin/env python3
# The shebang line should use the env program to find the python3 program.

# Purpose: Say hello

# These lines import various modules that the program needs.
import argparse  


# --------------------------------------------------
# The get_args() function is dedicated to getting the arguments.
# All the argparse code now lives here.
# The get_args() function is responsible for parsing and validating arguments.

def get_args():
    """Get the command-line arguments"""  # The docstring for the get_args() function.

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', default='World', help='Name to greet')
    return parser.parse_args() 
# We need to call return to send the results of parsing the arguments back to the main() function.


# --------------------------------------------------
# def defines a function, named main() in this case. The empty parentheses show that this function accepts no arguments.
# Define the main() function where the program starts.

def main():
    """Make a jazz noise here"""
#Call the get_args() function to get parsed arguments. If there is a problem with the arguments or if the user asks for --help, the program never gets to this point because argparse will cause it to exit. If our program does make it this far, the input values must 
# The first thing our main() functions will always do is call get_args() to get the arguments.

    args = get_args()
    print('Hello, ' + args.name + '!')


# --------------------------------------------------
# Every program or module in Python has a name that can be accessed through the variable __name__. When the program is being executed, the __name__ value will be equal to the text “__main__.”
 main()
if __name__ == '__main__':
    # If the condition is true, this calls the main() function.
    main()
