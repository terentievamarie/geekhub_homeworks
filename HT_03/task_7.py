# 7. Write a script which accepts a <number> from user and generates dictionary in range <number> where key is <number> and value is <number>*<number>
#    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

input_number = int(input("Please, enter a number: "))
dict_1 = {}

for i in range(input_number + 1):
    dict_1[i] = i**2
print(dict_1)