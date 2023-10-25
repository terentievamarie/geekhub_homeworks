"""
3. Write a script to concatenate following dictionaries to create a new one.
    dict_1 = {'foo': 'bar', 'bar': 'buz'}
    dict_2 = {'dou': 'jones', 'USD': 36}
    dict_3 = {'AUD': 19.2, 'name': 'Tom'}
"""

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
d_result = dict(list(dict_1.items()) + list(dict_2.items()) + list(dict_3.items())
    
print(d_result)

