# -*- coding: utf-8 -*-
"""
Two sorted array merge to single array sorted
"""

l1 = [1,3,9]
l2 = [2,5,7]

l3 = []

i=0
j=0

currentFirst = l1[i]
currentSecond = l2[j]
while True:
    if (currentFirst<currentSecond):
        l3.append(currentFirst)
        i +=1
        if i>=len(l1):
            break
        currentFirst = l1[i]
    elif currentFirst>currentSecond:
        l3.append(currentSecond)
        j+=1
        if j>=len(l2):
            break
        currentSecond = l2[j]

if i < len(l1):
    print('L1 not filled completely')
    for val in range(i,len(l1)):
        l3.append(l1[val])

if j < len(l2):
    print('L2 not filled completely')
    for val in range(j,len(l2)):
        l3.append(l2[val])