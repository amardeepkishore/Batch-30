#!/usr/bin/env python

__author__ = "Amar"

#Import Modules
import sys


Sure = raw_input("Need to Enter 3 Number with space to evaluate the highest of it, Do you want to continue(Y/N):> \n")

if Sure == 'N' or Sure == 'n':
    print("Exiting on user command")
    sys.exit(0)

while True:
    Input = []
    Input.extend(raw_input("You Chose to continue with the programme, Enter Exactly Three Numbers with Space:> ").split())

    Num1 = Input[0]
    print("First Value Entered {0}\n".format(Num1))
    Num2 = Input[1]
    print("Second Value Entered {0}\n".format(Num2))
    Num3 = Input[2]
    print("Third Value Entered {0}\n".format(Num3))

    Found = max(Input)

    if Num1 == Num2 == Num3:
        print("All Entered Vales are equal, The Value you entered {0}, {1}, and {2}.".format(Num1, Num2, Num3))
    else:
        print("Greater Number Entered by user is {}\n".format(Found))

    User_input = raw_input("Do you want to continue again (Y/N):> \n")

    if User_input == 'Y' or User_input == 'y':
        print("User Selected to continue.")
    else:
        break
