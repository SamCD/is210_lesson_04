#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
TEAM1 = []
TEAM2 = []
TEAM3 = []
x = 0
y = 0
z = 0
MP = data.MULTIPLAYERS.split("\n")[2:]

for i in range(len(MP)):
    if MP[i][-1] == "0":
        continue
    else:
        if len(TEAM1) == TEAM2 == TEAM3:
            TEAM1[x] = MP[i]
            x += 1
        elif TEAM2 == TEAM3:
             TEAM2[y] = MP[i]
            y += 1
        elif: TEAM
            TEAM3[z] = MP[i]
            z += 1
            if TEAM3 = 4
            break
