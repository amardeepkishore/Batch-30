#!/usr/bin/env python

__author__ = 'akishore'


'''
    This script will generate random sentences using pre-defined
    words.
    '''

import random
import sys
from os import system

Mlist = ['amar', 'nitin', 'shri',]
Flist = ['radha', 'rani', 'sweta']
Blist = ['sparrow', 'crow', 'vlture']
AMlist = ['dog', 'tiger', 'lion']
AFlist = ['cow','cat','goat']
Vlist = ['likes','hates','loves','wants']
Olist = ['gym','drug','swimming','dancing','badminton','hockey','eating','flying','chanting','hunting']
Clist = ['although','but','however','wheareas','despite','inspite of']
ADlist = ['he','she','it']

def mf():
    combi = [Mlist,Flist,Blist,AMlist,AFlist]
    combi_f = random.choice(random.choice(combi))
    return combi_f


def genrator():

    def adlist():
        return random.choice(ADlist)

    adlist_f = adlist()
    mf_f = mf()
    Wlist = [[mf_f.capitalize()],Vlist,Olist,Clist,[adlist_f.capitalize()],Vlist,Olist]
    Genrator = [random.choice(Iteration) for Iteration in Wlist]

    if mf_f in Mlist and adlist_f == 'he':
        return ' '.join(Genrator)

    elif mf_f in Flist and adlist_f == 'she':
        return ' '.join(Genrator)

    elif mf_f in Blist and adlist_f == 'it':
        return ' '.join(Genrator)

    elif mf_f in AMlist and adlist_f == 'he':
        return ' '.join(Genrator)

    elif mf_f in AFlist and adlist_f == 'she':
        return ' '.join(Genrator)

    else:
        print("Hilarious sentance, isn't it, '{}' is not '{}' right, press return to find more...\n".format(mf_f.upper(),adlist_f.upper()))
        return ' '.join(Genrator)

if __name__ == '__main__':

    system('clear')
    while True:

        Input = raw_input("To genrate random sentances press 'Y' or 'N' to exit the game:-> ")
        if Input == 'n' or Input == 'N':
            print("Exiting on user input")
            sys.exit(0)
        else:
            system('clear')

        print("Continueing on user demand. . .\n")

        print(genrator())
        print("")



