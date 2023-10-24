# 6. Write a script to get the maximum and minimum value in a dictionary.

dict_1 = {
    'id': 17,
    'name': 'NoName',
    'freeze': -35,
    'count': 1,
    'admin': False,
    'errors': [400, 403],
    'email': None,
    'salary': 3750,
    'speed': 75.8,
    'file': 100644,
}

max_value = dict_1['id']
min_value = dict_1['id']

for key, value in dict_1.items():
    if isinstance(value, (int, float, bool)):
        if max_value is None or value > max_value:
            max_value = value
        if min_value is None or value < min_value:
            min_value = value

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")