#!/usr/bin/env python

__author__ = 'akishore'


''' The family tree includes only the first names of female members of the family,
    mothers and daughters, through many generations. '''

# Importing Module
import sys
import re
from os import system
#ftree = {'anna':['a1','a2'], 'lazy':['b1','b2'], 'a1':['x1','x2'], 'x1':['z1','z2']}
ftree = {}

first = ''
second = ''


def systm_exit():
    print("Exiting on user input...")
    sys.exit(0)


def mem_tree():
    for i, j in ftree.iteritems():
        print(i)
        print('.'*len(i) + "|__ {}".format(j[0]))
        print('.'*len(i) + "|__ {}\n".format(j[1]))


def mem_add():
    keyorvalue = raw_input("If you want to add {} as a Mother type '1' and to add {} as a Daughter of other Mother\'s type '2'.: ".format(first.upper(),first.upper()))
    print("")
    if keyorvalue == '1':
        daughter_len = '0'
        while daughter_len != '2':
            daughter = raw_input("Type the daughter first names with space, it should not exceed more than 2 names.: ").split()
            print("")
            daughter_len = str(len(daughter))
            if daughter_len == '2':
                break
            print("Kindly provide exactly '2' values with spaces in between.\n")
        ftree[first] = daughter
    elif keyorvalue == '2':
        mothername = raw_input("To choose the name of mother from list type '1' to to provide new name type '2'.: ")
        if mothername == '1':
            print(ftree.keys())
            mothernew1 = raw_input("Type the name of the Mother of {}: ".format(first.upper()))
            ftree[mothernew1] = first
        elif mothername == '2':
            mothernew2 = raw_input("Type the name of the Mother of {}: ".format(first.upper()))
            ftree[mothernew2] = first
        else:
            print("make sure you type either '1' or '2' to proceed".upper())
    else:
        print("WRONG VALUE PROVIDED, TYPE EITHER '1' or '2\n")


def mem_search():
    global first
    first = raw_input("Type the name of first member: ")
    print("")
    if first in ftree.keys() or True in [first in ftree.values()[i] for i in range(len(ftree.values()))]:
        global second
        try:
            second = raw_input("Type the name of second member: ")
            print("")
            if second not in ftree.keys() and True not in [second in ftree.values()[i] for i in range(len(ftree.values()))] and False in [second in ftree.values()[i] for i in range(len(ftree.values()))] :
                sures = raw_input("{} is not found, do you want to add it now. 'y' or 'n': ".format(second.upper()))
                while True:
                    if re.match('^n$',sures,re.I):
                        systm_exit()
                    elif re.match('^y$',sures,re.I):
                        mem_add()
                    else:
                        print("Error: input not valid: Try again.\n")
            elif second in ftree.keys() and first in ftree.get(second):
                print("{} is mother of {}".format(second.upper(),first.upper()))
            elif first in ftree.keys() and second in ftree.get(first):
                print("{} is the mother of {}".format(first.upper(),second.upper()))
            elif  [first in ftree.values()[i] for i in range(len(ftree.values()))].index(True) == [second in ftree.values()[i] for i in range(len(ftree.values()))].index(True):
                mother = ftree.items()[[first in ftree.values()[i] for i in range(len(ftree.values()))].index(True)][0]
                print("{} and {} are sisters and their mother is {}".format(first.upper(),second.upper(),mother.upper()))
            else:
                print("No direct relation found, Try Again...\n")
        except ValueError:
            print("{} has not mother listed here, It means {} is the oldest lady".format(first.upper(),first.upper()))
    else:
        mem_add()

if __name__ == '__main__':
  system('clear')
  while True:
    sure = raw_input("Do you want to continue 'Yes' or 'No': ")
    if re.match('^no$|^n$',sure,re.I):
        systm_exit()

    elif re.match('^yes$|^y$',sure,re.I):
        print("You selected to continue with programme.\n")

        while True:
            userinput = raw_input("press '1' to display the family tree, '2' to display the relationship of two members or '3' to exit.: ")

            if userinput == '1':
                print("FAMILY TREE\n")
                mem_tree()
            elif userinput == '2':
                print("You chose to display the relationship of two members...\n")
                if not bool(ftree):
                    while True:
                        suren = raw_input("FAMILY TREE IS EMPTY,\t Do you want to create one. type 'Yes' to continue or 'No' to exit. ")
                        if re.match('^no$|^n$',suren,re.I):
                            systm_exit()
                        elif re.match('^yes$|^y$',suren,re.I):
                            print("You selected to add the member.\n")
                            mem_search()
                            break
                        else:
                            print("Wrong value provided, Either type 'Yes|Y' or 'No|N'. \n")
                else:
                    print("Family tree is not empty.\n")
                    mem_search()
            elif userinput == '3':
                systm_exit()
            else:
                print("Wrong value, Provide either '1' , '2' or '3'\n")

    else:
        print("Provide Input either 'Yes|Y' or 'No|N' ")

#while True:



