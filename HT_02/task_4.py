# 4. Write a script which accepts a <number> from user and then <number> times asks user for string input.
# At the end script must print out result of concatenating all <number> strings.

number = int(input("Please, enter a number: "))
list_of_strings = []

for i in range(number):
    input_str = input("Please, enter a string: ")
    list_of_strings.append(input_str)
print(f"Output string: {''.join(list_of_strings)}")
