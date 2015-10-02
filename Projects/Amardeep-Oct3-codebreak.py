#!/usr/bin/env python

__author__ = 'akishore'

import sys
from os import system

'''
    This script will reveal the acctual meaning of decrepted sentence
    Sentence to crypt: QM YR JYQR WMS YPC Y NWRFML ESW.
    expected answer:   So at last you are a python guy.

    '''

decrypt = 'QM YR JYQR WMS YPC Y NWRFML ESW'
alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfa1 = alfa[2:26] + alfa[0:2]

def string_dec(a):
    hashtable = {}
    for i,j in zip(alfa,alfa1):
        hashtable[ord(i)] = j
    return a.translate(hashtable)

print(string_dec(decrypt))
system('clear')

while True:
    Sure = input("Press 'Y' to continue or 'N' to Exit:->  \n")

    if Sure == 'N' or Sure == 'n':
        system('clear')
        print("Exiting on user command")
        sys.exit(0)

    Input = input("Provide the Letters or Sentences to Decrypt or type 'decrypt' to take default value:-> ")

    if Input == 'decrypt' or Input == 'DECRYPT' or Input == 'Decrypt':
        system('clear')
        print(string_dec(decrypt))
    elif Input:
        system('clear')
        print(string_dec(Input.upper()))
    else:
        system('clear')
        print("Noting Provided, Try Again\n")