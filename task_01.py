#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
TOTAL_WORDS = 0.00
NUM_LINES = 0.00
MAXIMUM_WORDS = 0
MINIMUM_WORDS = 0
for LINE in data.SHAKESPEARE.split("\n"):
    NUM_LINES += 1.00
    WORDS = LINE.split()
    WORD_CT = len(WORDS)
    if WORD_CT < MINIMUM_WORDS or MINIMUM_WORDS == 0:
        MINIMUM_WORDS = WORD_CT
    if WORD_CT > MAXIMUM_WORDS:
        MAXIMUM_WORDS = WORD_CT
    NUM_CRISPIAN = data.SHAKESPEARE.count("Crispian")
    TOTAL_WORDS += len(WORDS)
AVERAGE_WORDS = TOTAL_WORDS / NUM_LINES


print "\n *** min number of words in a line = " + str(MINIMUM_WORDS)
print "\n *** max number of words in a line = " + str(MAXIMUM_WORDS)
print "\n *** Amt of times the word 'Crispian' occurs = " + str(NUM_CRISPIAN)
print "\n *** Avg words per line = " + str(AVERAGE_WORDS)

