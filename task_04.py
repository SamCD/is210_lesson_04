#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
TEAM1 = []
TEAM2 = []
TEAM3 = []
MP = data.MULTIPLAYERS.split("\n")[1:]

for i in range(len(MP)):
    if len(TEAM3) == 4:
        break
    elif MP[i][-1] == "0":
        continue
    else:
        if len(TEAM1) == len(TEAM2) == len(TEAM3):
            TEAM1.append(MP[i][:-1].strip())
        elif len(TEAM2) == len(TEAM3):
            TEAM2.append(MP[i][:-1].strip())
        elif len(TEAM3) < len(TEAM2):
            TEAM3.append(MP[i][:-1].strip())
    
print "Team 1 =", TEAM1, "Team 2 =", TEAM2, "Team 3 =", TEAM3
