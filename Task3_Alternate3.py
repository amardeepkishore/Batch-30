#!/usr/bin/env python

__author__ = "Amar"

# Given List To Be Changed.
days = ['yesterday', 'today', 'tomorrow', 'dayafter', 'amardeep']

print(days) # Printing the initial list.

for Index_val in days:                                              # Simple loop to save the object of list as string in variable.
    Index_num = days.index(Index_val)                               # Extracting the Index number from the List using the object saved above.
    day = Index_val[:Index_num+1].upper() + Index_val[Index_num+1:] #Concatinating, Modifying and Adding back the original string.
    days[Index_num] = day                                           #Finally updating original List with new values

# Printing the new list
print(" ")
print(days)