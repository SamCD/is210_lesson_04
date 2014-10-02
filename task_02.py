#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a password protection"""

import data
ACCESS = False
while ACCESS is False:
    X = raw_input("What is your password? (Attempt 1/3)")
    if X == data.PASSWORD:
        ACCESS = True
        print "Access granted"
        break
    elif X != data.PASSWORD:
        X = raw_input("What is your password? (Attempt 2/3)")
        if X == data.PASSWORD:
            ACCESS = True
            print "Access granted"
            break
        elif X != data.PASSWORD:
            X = raw_input("What is your password? (Final attempt)")
            if X == data.PASSWORD:
                ACCESS = True
                print "Access granted"
                break
            elif X != data.PASSWORD:
                print "Access denied, try again later"
                break
