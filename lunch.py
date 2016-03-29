#!/usr/bin/python2
#
#
# Created by: Kyle Walker
# 
# Purpose: Make a lunch decision 

#Necessary Libraries
from random import randint
from random import randrange
from pyfiglet import figlet_format
import operator

#variables for restaurants
pdq = 0
torchys = 0
mods = 0
freebirds = 0
canes = 0
mypizzaria = 0
whataburger = 0
potbelly = 0
tacobell = 0
smash = 0
juanitas = 0
arbys = 0
chickfila = 0
jimmyjohns = 0
popeyes = 0

totalsdic = {"pdq":pdq,"torchys":torchys,"mods":mods,"freebirds":freebirds,"canes":canes,"mypizzaria":mypizzaria,"whataburger":whataburger,"potbelly":potbelly,"tacobell":tacobell,"smash":smash,"juanitas":juanitas,"arbys":arbys,"chickfila":chickfila,"jimmyjohns":jimmyjohns,"popeyes":popeyes}

#functions
def printline():
    print "[*]----------------------------[*]"

def banner():
    printline()
    print "[*]===-->=LUNCH DECISION=<--===[*]"
    printline()

def randino():
    return randrange(1,16)
    #print randint(1,16)

def counting():
    #handles the actual logic and counting for the vars
    global pdq
    global torchys
    global mods
    global freebirds
    global canes
    global mypizzaria
    global whataburger
    global potbelly
    global tacobell
    global smash
    global juanitas
    global arbys
    global chickfila
    global jimmyjohns
    global popeyes

    count = 1

    while (count <= 9999):
        x = randino()
        if x  == 1:
            totalsdic["pdq"] += 1
        elif x  == 2:
            totalsdic["torchys"] += 1
        elif x  == 3:
            totalsdic["mods"] += 1
        elif x  == 4:
            totalsdic["freebirds"] += 1
        elif x  == 5:
            totalsdic["canes"] += 1
        elif x  == 6:
            totalsdic["mypizzaria"] += 1
        elif x  == 7:
            totalsdic["whataburger"] += 1
        elif x  == 8:
            totalsdic["potbelly"] += 1
        elif x  == 9:
            totalsdic["tacobell"] += 1
        elif x  == 10:
            totalsdic["smash"] += 1
        elif x  == 11:
            totalsdic["juanitas"] += 1
        elif x  == 12:
            totalsdic["arbys"] += 1
        elif x  == 13:
            totalsdic["chickfila"] += 1
        elif x  == 14:
            totalsdic["jimmyjohns"] += 1
        elif x  == 15:
            totalsdic["popeyes"] += 1
        count += 1
        
def outputwinner():
    #prints out in pretty words the outcome
    choice = max(totalsdic.iteritems(), key=operator.itemgetter(1))[0]
    banner() 
    print figlet_format(choice)

def waschosen(x):
    #function to mark if you actually chose the lunch choice. 
    chosen = False
    if raw_input("Was %s chosen? [y/n] " % x) == "y":
        chosen = True
        print "%s marked as chosen, good luck" % x
        print "Writing down in tally for week that %s was chosen" % x

counting()
outputwinner()
