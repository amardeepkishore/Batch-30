#!/usr/bin/env python

__author__ = 'akishore'

days = ['yesterday', 'today', 'tomorrow', 'dayafter']

for Index in days:
    Index_num = days.index(Index)
    day = (days[Index_num])

    for Index_loop in range(Index_num):
        day_val = list(day[0:Index_num+1].upper())
        day = list(day)

        for Index_update in range(Index_num+1):
            day[Index_update] = day_val[Index_update]

        limiter = ''
        day = limiter.join(day)
        days[Index_num] = day

print(days)
