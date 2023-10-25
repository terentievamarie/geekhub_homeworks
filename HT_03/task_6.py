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
    'e': [-12, -336],
    'e1': 'Ra'
}

max_value = float('-inf')
min_value = float('inf')
max_value_str = None
min_value_str = None
max_value_list = float('-inf')
min_value_list = float('inf')

for key, value in dict_1.items():
    if isinstance(value, (int, float, bool)):
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    if isinstance(value, str):
        if max_value_str is None or len(value) > len(max_value_str):
            max_value_str = value
        if min_value_str is None or len(value) < len(min_value_str):
            min_value_str = value
    if isinstance(value, list):
        if max(value) > max_value_list:
            max_value_list = max(value)
        if min(value) < min_value_list:
            min_value_list = min(value)


print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Maximum str value: {max_value_str}")
print(f"Minimum str value: {min_value_str}")
print(f"Maximum value in list: {max_value_list}")
print(f"Minimum value in list: {min_value_list}")
