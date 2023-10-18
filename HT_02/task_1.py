#1. Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numbers = list(map(int, input().split(", ")))
numbers_tuple = tuple(numbers)
print(f"List: {numbers}")
print(f"Tuple: {numbers_tuple}")