# This file is for working with dictionaries in python

import numpy as np

dict = {}

dict['python'] = ['ali','bita']
dict['java'] = ['book','pc','android']
dict['C++'] = ['rrrr', 'fast']
dict['ruby'] = ['web']

a  = dict['java'] + dict['ruby']
print a

c = 'test'
tags = 'python,java,ruby'

print '========='
print tags.split(',')
print '========='

for t in tags.split(','):
	tmp = dict[t]
	tmp.append(c)
	dict[t] = tmp

print dict['python']

## saving the dictionary to a file
np.save('myFile.npy', dict)

## Loading the dictionary
loadeddict = np.load('myFile.npy').item()
print loadeddict.keys()

loadeddict['newkey'] = ['val1', 'val2']

print loadeddict.keys()
print loadeddict['newkey']