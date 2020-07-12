#!/usr/bin/python3
from random import randrange
#assumes people have pyfiglet libs
try:
    from pyfiglet import figlet_format
    def banner(x):
        print("[*]----------------------------[*]")
        print(figlet_format(x))
        print("[*]----------------------------[*]")
#if no pyfiglet, just print basic
except ImportError:
    def banner(x):
        print("[*]----------------------------[*]")
        print(x)
        print("[*]----------------------------[*]")

def lunch():
    #this is a dic, examp: {1:"choice",2:"choice2"}
    choices = {1:"Whataburger",2:"Jack in the Box",3:"Jason's Deli",4:"Jimmy Johns"}
    #makes the choice based on randrange adding 1 (to avoid a 0 result)
    banner(choices[randrange(len(choices))+1])

lunch()
