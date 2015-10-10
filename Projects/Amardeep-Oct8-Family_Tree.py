#!/usr/bin/env python

__author__ = 'akishore'


'''
The family tree includes only the first names of female members of the family,
    mothers and daughters, through many generations.

This function will take three* parameters:
    1. A string representing the family tree
    2. The name of the first person
    3. The name of another person

* Follow the instructions for more legibility.

Here are several examples of different pairs of people and the result for the tree as above:
    1. IN: Hazel & Gloria             OUT: Clare             (they have a direct common mother)
    2. IN: Hazel & Clare              OUT: Clare             (one is the mother of the other)
    3. IN: Hazel & Flora              OUT: Ann                (closest is their grandmother)
    4. IN: Hazel & Betty              OUT: Ann                (the only ancestor in common is Ann)
    5. IN: Hazel & Ann                OUT: Ann                (one is the grandmother of the other)
    6. IN: Hazel & Hazel             OUT: Hazel              (they are the same person - just return that person)

Note:- This Programme will give you more verbosity than the user cases shown above and a functionality to add new members too.
'''

# Importing Module
import sys
import re
from os import system

ftree = {"Ann": ["Betty", "Clare"], "Betty": ["Donna", "Elizabeth", "Flora"], "Clare": ["Gloria", "Hazel"]}
# ftree = {}

# Global Declaration for user input.
first = ''
second = ''

# Below variable should be used only one time in programme.
_mother1 = ''
_mother2 = ''


# System Exit function.
def systm_exit():
    print("Exiting on user input...")
    sys.exit(0)


# Finding Mother of Input Function.
def find_mother():
    try:
        if True in [first in ftree.values()[i] for i in range(len(ftree.values()))]:
            global _mother1
            _mother1 = ftree.items()[[first in ftree.values()[i] for i in range(len(ftree.values()))].index(True)][0]
            return _mother1
        elif True in [second in ftree.values()[i] for i in range(len(ftree.values()))]:
            global _mother2
            _mother2 = ftree.items()[[second in ftree.values()[i] for i in range(len(ftree.values()))].index(True)][0]
            return _mother2
    except ValueError:
        return "No Mother Found".upper()


# Finding Grandmother of Mother function.
def find_gmother():
    try:
        if first in ftree.get(find_mother()):
            grandmother1 = ftree.items()[[_mother1 in ftree.values()[i] for i in range(len(ftree.values()))].index(True)][0]
            return grandmother1
        elif second in ftree.get(find_mother()):
            grandmother2 = ftree.items()[[_mother2 in ftree.values()[i] for i in range(len(ftree.values()))].index(True)][0]
            return grandmother2
    except ValueError:
        return "No One".upper()


# List The Families Tree
def mem_tree():
        for i, j in ftree.iteritems():
            print(i)
            for k in range(len(j)):
                    print('.'*len(i) + "|__ {}".format(j[k]))
            print("")


# Add new members if not found in List.
def mem_add():
    keyorvalue = raw_input("If you want to add {} as a Mother type '1'\
 and to add {} as a Daughter of other Mother\'s type '2'.: ".format(first.upper(), first.upper()))
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


# Mem Add simplified.
def mem_add_sure():
    sures = raw_input("{} is not found, do you want to add it now. 'y' or 'n': ".format(second.upper()))
    while True:
        if re.match('^n$',sures,re.I):
            return systm_exit()
        elif re.match('^y$',sures,re.I):
            return mem_add()
        else:
            return "Error: input not valid: Try again.\n"


def case1():
    try:
        if [first in ftree.values()[i] for i in range(len(ftree.values()))].index(True) == [second in ftree.values()[i] for i in range(len(ftree.values()))].index(True):
            xyz = "{} and {} are Sisters and their Mother and Grandmother are {} and {} respectively.\n".format(first.upper(), second.upper(), find_mother(), find_gmother())
        return xyz
    except:
        pass


def case2():
    try:
        if second in ftree.keys() and first in ftree.get(second):
            return "{} is mother of {}\n".format(second.upper(),first.upper())
        elif first in ftree.keys() and second in ftree.get(first):
            return "{} is the mother of {}\n".format(first.upper(),second.upper())
    except:
        pass


def case3():
    try:
        if (first not in ftree.keys() or second not in ftree.keys())\
                and ([first in ftree.values()[i] for i in range(len(ftree.values()))][[first in ftree.values()[i] for i in range(len(ftree.values()))].index(True)]\
                or [second in ftree.values()[i] for i in range(len(ftree.values()))][[second in ftree.values()[i] for i in range(len(ftree.values()))].index(True)]) is True:
            return "{} and {}'s closest is their Grandmother {}.\n ".format(first, second, find_gmother())
    except:
        pass


def case4():
    try:
        if first not in ftree.keys() and\
                ([second in ftree.values()[i] for i in range(len(ftree.values()))][[second in ftree.values()[i] for i in range(len(ftree.values()))].index(True)] is True\
                and second in ftree.keys()) or second not in ftree.keys() and ([first in ftree.values()[i] for i in range(len(ftree.values()))][[first in ftree.values()[i]\
                for i in range(len(ftree.values()))].index(True)] is True and first in ftree.keys()):
            return "The Only Ancestor Common between {} and {} is {}.\n ".format(first, second, find_gmother())
    except:
        pass


def case5():
    try:
        if (first not in ftree.keys() and second in ftree.keys()) and second not in [j for j in [i for i in ftree.values()] if second not in j][0]:
            return "{} is the Grandmother of {}\n".format(second, first)
        elif second not in ftree.keys() and first in ftree.keys() and first not in [j for j in [i for i in ftree.values()] if first not in j][0]:
            return "{} is the Grandmother of {}".format(first, second)
    except:
        pass


def case6():
    try:
        if first == second:
            return "Both typed name is {}, A same Person/Name.".format(first)
    except:
        pass


def mem_search():
    global first
    first = raw_input("Type the name of first member: ").capitalize()
    print("")

    if first in ftree.keys() or True in [first in ftree.values()[i] for i in range(len(ftree.values()))]:
            global second
            second = raw_input("Type the name of second member: ").capitalize()

            if second not in ftree.keys() and True not in [second in ftree.values()[i] for i in range(len(ftree.values()))]:
                mem_add_sure()
            else:

                if case6() is not None:
                    print(case6())

                elif case1() is not None:
                    print(case1())

                elif case2() is not None:
                    print(case2())

                elif case4() is not None:
                    print(case4())

                elif case5() is not None:
                    print(case5())

                elif case3() is not None:
                    print(case3())
    else:
        mem_add_sure()


# Main Programme which calls() all above functions as per requirement.
if __name__ == '__main__':
  system('clear')
  while True:
    sure = raw_input("Do you want to continue 'Yes' or 'No': ")
    if re.match('^no$|^n$', sure, re.I):
        systm_exit()

    elif re.match('^yes$|^y$', sure, re.I):
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
                        if re.match('^no$|^n$', suren, re.I):
                            systm_exit()
                        elif re.match('^yes$|^y$', suren, re.I):
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