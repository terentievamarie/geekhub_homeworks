"""
Create a custom exception class called NegativeValueError.
Write a Python program that takes an integer as input 
and raises the NegativeValueError if the input is negative. 
Handle this custom exception with a try/except block 
and display an error message.
"""

class NegativeValueError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value
    
    def __str__(self):
        return f"{self.input_value} is not allowed"
    

try:
    number_1 = int(input("Please enter a number: ")) 
    if number_1 < 0:
        raise NegativeValueError(number_1)
    print(f"{number_1} is allowed")
except NegativeValueError as error:
    print(error)
