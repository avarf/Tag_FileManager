import json

dict = {}

dict['python'] = ['ali','bita']
dict['java'] = ['book','pc','android']
dict['C++'] = ['rrrr', 'fast']
dict['ruby'] = ['web']


json.dump(dict, open("text.txt",'w'))

loadeddict = json.load(open("text.txt"))

print type(loadeddict)
print loadeddict['java']