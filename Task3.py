#!/usr/bin/env python

__author__ = 'akishore'

days = ['yesterday', 'today', 'tomorrow', 'dayafter']

Index1 = days[0]
Index2 = days[1]
Index3 = days[2]
Index4 = days[3]

Index1_list = list(Index1)
Index2_list = list(Index2)
Index3_list = list(Index3)
Index4_list = list(Index4)

Index1_var = Index1[0:1]
Index1_var = Index1.upper()
Index1_var = list(Index1_var)

Index1_list[0] = Index1_var[0]

limiter = ''
Index1_list = limiter.join(Index1_list)
print(Index1_list)


Index2_var = Index2[0:2]
Index2_var = Index2.upper()
Index2_var = list(Index2_var)

Index2_list[0] = Index2_var[0]
Index2_list[1] = Index2_var[1]

limiter = ''
Index2_list = limiter.join(Index2_list)
print(Index2_list)


Index3_var = Index3[0:3]
Index3_var = Index3.upper()
Index3_var = list(Index3_var)

Index3_list[0] = Index3_var[0]
Index3_list[1] = Index3_var[1]
Index3_list[2] = Index3_var[2]

limiter = ''
Index3_list = limiter.join(Index3_list)
print(Index3_list)

Index4_var = Index4[0:4]
Index4_var = Index4_var.upper()
Index4_var = list(Index4_var)

Index4_list[0] = Index4_var[0]
Index4_list[1] = Index4_var[1]
Index4_list[2] = Index4_var[2]
Index4_list[3] = Index4_var[3]

limiter = ''
Index4_list = limiter.join(Index4_list)
print(Index4_list)

days = [Index1_list, Index2_list, Index3_list, Index4_list]
print(days)