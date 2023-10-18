# 7. Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and integers and must be hardcoded.

hardcoded_list = [True, 3, "Alina", "Ali", 7, False, "Python"]
result = ''.join([str(i) for i in hardcoded_list])
print(result)