#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
ACCESS = False
while ACCESS == False:
    x = raw_input("What is your password? (Attempt 1/3)")
    if x == data.PASSWORD:
        ACCESS = True
        print "Access granted"
        break
    elif x != data.PASSWORD:
        x = raw_input("What is your password? (Attempt 2/3)")
        if x == data.PASSWORD: 
            ACCESS = True
            print "Access granted"
            break           
        elif x != data.PASSWORD:
            x = raw_input("What is your password? (Final attempt)")
            if x == data.PASSWORD: 
                ACCESS = True
                print "Access granted"
                break
            elif x != data.PASSWORD:
                print "Access denied, try again later"
                break
                

                
    
