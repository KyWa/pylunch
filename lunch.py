#!/usr/bin/python2
from random import randrange
try:
    from pyfiglet import figlet_format
    def banner(x):
        print "[*]----------------------------[*]"
        print figlet_format(x)
        print "[*]----------------------------[*]"

except ImportError:
    def banner(x):
        print "[*]----------------------------[*]"
        print x
        print "[*]----------------------------[*]"

def lunch():
    choices = {1:"PDQ",2:"Torchys",3:"MOD",4:"Freeibrds",5:"Popeyes",6:"My Pizzaria",7:"Whataburger",8:"Taco Bell",9:"Arbys",10:"Smash Burger",11:"Potbellys"} 
    banner(choices[randrange(len(choices)+1)])

lunch()
