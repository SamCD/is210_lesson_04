#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
SHAKE1 = data.SHAKESPEARE.split("\n")
MAXIMUM_WORDS = 0
for line in SHAKE1:
    y = (line).split(" ")
    if len(y) > MAXIMUM_WORDS:
        MAXIMUM_WORDS = len(y)
print "\n *** max number of words in a line = " + str(MAXIMUM_WORDS)

import data
SHAKE1 = data.SHAKESPEARE.split("\n")
MINIMUM_WORDS = MAXIMUM_WORDS
for line in SHAKE1:
    y = (line).split(" ")
    if len(y) < MINIMUM_WORDS:
        MINIMUM_WORDS = len(y)
print "\n *** min number of words in a line = " + str(MINIMUM_WORDS)

SHAKE2 = data.SHAKESPEARE.split()
AVERAGE_WORDS = float(len(SHAKE2) / len(SHAKE1))
