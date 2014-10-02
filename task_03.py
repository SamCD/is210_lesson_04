#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Finding the minimimum and maximum daily amounts for a set of transactions"""

import data
TOTAL = 0
TRAN = data.TRANSACTIONS
for i in range(len(TRAN)):
    for j in range(len(TRAN[i])):
        TOTAL += TRAN[i][j]
print TOTAL

MINIMUM = 0
for i in range(len(TRAN)):
    x = 0
    for j in range(len(TRAN[i])):
        x += TRAN[i][j]
        if x < MINIMUM:
            MINIMUM = x
        else:
            continue
print MINIMUM

MAXIMUM = 0

for t in range(len(TRAN)):
    y = 0
    for s in range(len(TRAN[t])):
        y += TRAN[t][s]
        if MAXIMUM <= y:
            MAXIMUM = y
        else:
            continue
print MAXIMUM
