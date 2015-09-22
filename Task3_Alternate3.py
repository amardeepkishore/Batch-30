#!/usr/bin/env python

__author__ = "Amar"

days = ['yesterday', 'today', 'tomorrow', 'dayafter', 'amardeep']

print(days)

for Index_val in days:
    Index_num = days.index(Index_val)
    day = Index_val[:Index_num+1].upper() + Index_val[Index_num+1:]
    days[Index_num] = day

print(days)