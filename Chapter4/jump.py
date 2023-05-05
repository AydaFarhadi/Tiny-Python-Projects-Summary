#!/usr/bin/env python3
import argparse 

def get_args():
    parser=argparse.ArgumentParser(description='jump the five', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',help='input text', type=str,metavar='str')
    return parser.parse_args()



def main():
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
    main()