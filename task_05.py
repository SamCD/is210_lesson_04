#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a set of matchups"""

import data
MATCHUPS = []
COUNTER = 0
for ROW_INDEX, ROW_NAME in enumerate(data.VERSUS):
    for COLUMN_INDEX, COLUMN_NAME in enumerate(data.VERSUS):
        if ROW_INDEX > COLUMN_INDEX:
            COUNTER += 1
            MATCH = '{COUNTER},"{0}","{1}"'.format(ROW_NAME, \
            COLUMN_NAME, COUNTER=COUNTER)
            MATCHUPS.append(MATCH)
MATCHUPS = '\n'.join(MATCHUPS)
print MATCHUPS
