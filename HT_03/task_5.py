# 5. Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

dict_1 = {1: "apple", 2: "banana", 3: "pizza", 4: "apple", 5: "pineapple", 6: "banana"}
dict_unique = {}

[dict_unique.update({k:v}) for k,v in dict_1.items() if v not in dict_unique.values()]
print(dict_unique)