#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating teams"""

import data
TEAM1 = []
TEAM2 = []
TEAM3 = []
MP = data.MULTIPLAYERS.split("\n")[1:]
Y = 0

for i in range(len(MP)):
    if len(TEAM3) == 4:
        break
    elif MP[i][-1] == "0":
        continue
    else:
        Y += 1
        if Y % 3 == 1:
            TEAM1.append(MP[i][:-1].strip())
        elif Y % 3 == 2:
            TEAM2.append(MP[i][:-1].strip())
        elif Y % 3 == 0:
            TEAM3.append(MP[i][:-1].strip())
TEAM1 = ",".join(TEAM1)
TEAM2 = ",".join(TEAM2)
TEAM3 = ",".join(TEAM3)

print "Team 1 =", TEAM1, "\nTeam 2 =", TEAM2, "\nTeam 3 =", TEAM3
