# 4. Write a script that combines three dictionaries by updating the first one.

dict_1 = {"list": [1, 2, 3], "tuple": (1, 5, 4)}
dict_2 = {"bool": True, "string": "string"}
dict_3 = {"int": 1, "float": 3.4}

dict_1.update(dict_2)
dict_1.update(dict_3)

print(dict_1)
