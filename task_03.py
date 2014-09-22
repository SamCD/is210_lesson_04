#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
TOTAL = 0
trans = data.TRANSACTIONS
for i in range(len(trans)):
    for j in range(len(trans[i])):
        TOTAL += trans[i][j]
print TOTAL

MINIMUM = 0
x = 0
for i in range(len(trans)):
    for j in range(len(trans[i])):
        x += trans[i][j]
        if MINIMUM <= x:
            continue
        else: MINIMUM = x
print MINIMUM

MAXIMUM = 0
y = 0
for i in range(len(trans)):
    for j in range(len(trans[i])):
        y = sum(trans[i][:-1])
        if MAXIMUM >= y:
            continue
        else: MAXIMUM = y
        break
print MAXIMUM
