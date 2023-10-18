# 6. Write a script to check whether a value from user input is contained in a group of values.
#    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#         [1, 2, 'u', 'a', 4, True] --> 5 --> False

list_1 = [1, 2, 'u', 'a', 4, True]
user_value = input("Please, enter your value: ")
list_of_strings = [str(i) for i in list_1]
print(user_value in list_of_strings)