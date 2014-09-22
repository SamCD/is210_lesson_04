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
    x = 0
    for j in range(len(trans[i])):
        x += trans[i][j]
        if x < MINIMUM:
            MINIMUM = x
        else:
            continue
print MINIMUM

MAXIMUM = 0

for t in range(len(trans)):
    y = 0
    for s in range(len(trans[t])):
        y += trans[t][s]
        if MAXIMUM <= y:
            MAXIMUM = y
        else:
            continue
print MAXIMUM
