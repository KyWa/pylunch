#!/usr/bin/python2
from random import randrange
#assumes people have pyfiglet libs
def banner(x):
    print("[*]----------------------------[*]")
    print(x)
    print("[*]----------------------------[*]")

def lunch():
    #this is a dic, examp: {1:"choice",2:"choice2"}
    choices = {1:"McDonalds",2:"Whataburger",3:"Jack in the Box",4:"Jimmy Johns",5:"Five Guys",6:"Chick-fil-a"}
    #makes the choice based on randrange adding 1 (to avoid a 0 result)
    banner(choices[randrange(len(choices))+1])

lunch()
