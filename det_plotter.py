#! /usr/bin/env python

# This script plots determinant outputs from ACI

import sys
import csv
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from random import uniform

d_row = int(sys.argv[1])
row_count = 0
source = list()

# Grab the user-specified block of data
# and store it as a vector of lines.
#	
# The space-counting starts at 1,
# meaning that the command line arg
# should be 1 for the first P space.
	
with open("det_list.txt","r") as file_in:
	for n, line in enumerate(file_in):
		if len(line.strip()) == 0:
			row_count = row_count + 1
			continue
		if d_row == row_count:
			source.append(line.split())
		if row_count > d_row:
			break			
file_in.close()
# end file read

# Now we grab the data from the block
# and put it in the correct container

# For the determinants, we need ALL of them
# from each cycle to ensure unique labelling
det_map = {"":""}
det_counter = 0
with open("det_list.txt","r") as file_in:
	for n,line in enumerate(file_in):
		if len(line.strip()) == 0:
			continue
		else:
			this_line = line.split()
			if this_line[0] in det_map:
				continue
			else:
				det_map[this_line[0]] = det_counter
				det_counter = det_counter + 1
file_in.close()

# Read the coefficients and couplings from the relevant subblock
weights = {"":""}
couplings = { "" : "" }
det_labels = { "" : "" }
i = 0
for item in source:
	weights[item[0]] = float(item[1])
	det_labels[item[0]] = i
	for j in range(len(item) - 2):
		couplings[(i,j)] = abs(float(item[j+2])) 
	i = i + 1
del weights[""]
del couplings[""]
del det_labels[""]

G = nx.complete_graph(det_counter)

# plot the nodes

pos=nx.spring_layout(G)
for i in det_labels.keys():
	nx.draw_networkx_nodes(G, pos, nodelist=[det_labels[i]], node_size=100, alpha = weights[i],node_color='#16469D')

# Need to compute max coupling to normalize alpha values
max_couple = max(couplings.values())

for i in weights.keys():
	for j in weights.keys():
		if i ==j :
			continue
		else:
			#print str(det_map[dets[i]]) + "   " + str(det_map[dets[j]]) + "   " + str(couplings[(i,j)])
			nx.draw_networkx_edges(G, pos,edgelist=[ (det_labels[i], det_labels[j]) ],alpha= couplings[(det_labels[i],det_labels[j])] )	

ax = plt.subplot()
#ax.set_theta_zero_location('N')
#ax.xaxis.grid(False)
#ax.set_yticks([0,1])
#ax.set_rmax(1.1)
#ax.set_rlim(0)
#ax.set_yticklabels([])
#ax.set_xticklabels([])
#
#ax.set_rscale('symlog')
#
#ax.spines['polar'].set_visible(False)
#nx.draw_random(G)
#plt.show()
#ax.spines['top'].set_visible(False)
#ax.spines['bottom'].set_visible(False)
#ax.spines['left'].set_visible(False)
#ax.spines['right'].set_visible(False)

plt.rcParams['figure.figsize'] =  3.375, 2.25
plt.axis('off')
plt.savefig('web_' + str(d_row) + '.pdf',bbox_inches='tight')
