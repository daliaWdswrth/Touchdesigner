import csv
import sys
import random
import numpy

#Constants
table = op('null1')
table_info = op('info1')
n_rows = int(table_info['num_rows'])
n_cols = int(table_info['num_cols'])

t_list = list()
w_list = list()

#Get all wind speeds
for i in range(n_rows):
	elem = (table[i+1, 2])
	try:
		elem_i = int(elem)
	except:
		break
	w_list.append(elem_i)
	
#New array with all wind speeds
w_arr = numpy.array(w_list)

#Cycle through wind speeds - constantly cycles through values (output to chop?)
#Can't do the above bc Touchdesigner hates cycles/infinite loops :/

#Generate random weather values to lfo offset (on key 1 click)
if op('keyboardin1')['k1'] == 1:
	op('lfo1').par.offset = numpy.random.choice(w_arr, replace=False) * 10
	
#Alter mass of particles (default = 10) [on key click 2]
if op('keyboardin1')['k2'] == 1:
	print("CLICK 2")
	op('particle1').par.mass = numpy.random.choice(w_arr, replace=False) / 10

#Get all temperatures
for i in range(n_rows):
	elem = (table[i+1, 1])
	try:
		elem_i = int(elem)
	except:
		break
	t_list.append(elem_i)
	
#New array with all temperatures
t_arr = numpy.array(t_list)

#Generate random temperatures to lfo amplitude (on key 1 click)
if op('keyboardin1')['k1'] == 1:
	op('lfo1').par.amp = numpy.random.choice(t_arr, replace=False) / 1000
	
#Alter birth of particles (default = 10) [on key click 2]
if op('keyboardin1')['k2'] == 1:
	op('particle1').par.birth = numpy.random.choice(t_arr, replace=False) * 10
	if op('particle1').par.birth > 50:
		op('particle1').par.birth = numpy.random.choice(t_arr, replace=False) / 10
	
#Reset birth of particles [on key click 2]
if op('keyboardin1')['k3'] == 1:
	op('particle1').par.birth = 7.8


#Print statements for testing 
debug(table[0,0])
debug(n_rows)