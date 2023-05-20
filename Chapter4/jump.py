#!/usr/bin/env python3
import argparse 

def get_args():
    """
    1. Use argparse. we create parser object from argparse library that is imported and use its functions
    2. Use "add_argument" function to get argument from user. Here argument is text. 
    """
    parser=argparse.ArgumentParser(description='jump the five', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',help='input text', type=str,metavar='str')
    return parser.parse_args()



def main():
    """
    we can test functionality of program using hard coded argument as shown below
    Add encoding table.Dictionaires are like table with column names and key and values 
    get text from aprser and encode its characters and then save them on new string
    return newly created string
    """
    #argv="867-5309"
    args=get_args()
    encodings={
        '1':'9','2':'8','3':'7','4':'6','5':'0','6':'4','7':'3','8':'2','9':'1','0':'5'
    }

    passage=args.text
    new_text=''

    for char in passage:
        new_text+=encodings.get(char,char)
    
    #enlist=[x for x in passage]
    #my_output=[]
    # for i in list(passage):
    #     if i in encodings.keys():
    #         i=encodings[i]
    #     my_output.append(i)
    #print(passage)\
    return new_text


if __name__=='__main__':
    """
    main function is main part of every code that runs everyhting together. 
    There could be alot of other dependent files but at the end main runs final program
    """
    main()
