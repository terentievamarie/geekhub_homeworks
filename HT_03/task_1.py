"""
Write a script that will run through a list of tuples and replace the last
value for each tuple. The list of tuples can be hardcoded. The "replacement"
value is entered by user. The number of elements in the tuples must be different.
""" 

input_value = input("Please, enter your value: ")
list_of_tuples = [
    (1, True, "Python", 3.4, "One"),
    (3, 3.1, "String", "It's cool", False),
    (True, False, 2, 3, "Name", 444, "Three", "geekhub", 4.55555)
]

for i in range(len(list_of_tuples)):
    list_of_tuples[i] = tuple(list_of_tuples[i][:-1] + (input_value,))

print(list_of_tuples)

