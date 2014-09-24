#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
MATCHUPS = ""
COUNTER = 0
for ROW_INDEX, ROW_NAME in enumerate(data.VERSUS):
    for COLUMN_INDEX, COLUMN_NAME in enumerate(data.VERSUS):
        if ROW_INDEX > COLUMN_INDEX:
            COUNTER += 1
            MATCHUPS.append(COUNTER, "{0}", "{1}".format(ROW_NAME, COLUMN_NAME)
print MATCHUPS.strip()
