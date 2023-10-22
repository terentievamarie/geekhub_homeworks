# 6. Write a script to get the maximum and minimum value in a dictionary.

dict_1 = {'a': 1, 'b': 65, 'c': 55, 'd': -12, 'e': 98, 'f': -101}

min_1 = dict_1['a']
max_1 = dict_1['a']
dict_result = {}

for k, v in dict_1.items():
	if dict_1[k] < min_1:
		dict_result['min'] = v 

for k, v in dict_1.items():
	if dict_1[k] > max_1:
		dict_result['max'] = v
		
print(dict_result)

