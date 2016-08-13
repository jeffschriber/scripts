#!/usr/bin/env python

import re
import sys
import numpy as np

states =  sys.argv[1:]

for state_1 in states:
    for state_2 in states:

        if( state_2 < state_1 ):
            continue        

        datafile_0 = np.loadtxt("final_wfn_" + state_1 + ".txt",dtype=str)
        
        wfn_0 = {}
        
        for line in datafile_0:
            wfn_0[line[0]] = [line[1],line[2]]
        
        
        datafile_1 = np.loadtxt("final_wfn_" + state_2 + ".txt",dtype=str)
        
        wfn_1 = {}
        
        for line in datafile_1:
            wfn_1[line[0]] = [line[1],line[2]]
        
        
        # Compute the overlap
        overlap = 0.0
        for key, value in wfn_0.iteritems():
            if key in wfn_1:
                overlap = overlap + (float(wfn_1[key][0]) * float(value[0]))
        
        print "<" + state_1 + "|" + state_2 + "> = " + str(overlap) + "\n"
