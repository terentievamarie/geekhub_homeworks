"""
Write a Python program that demonstrates exception chaining.
Create a custom exception class called CustomError 
and another called SpecificError. 
In your program (could contain any logic you want),
raise a SpecificError, and then catch it in a try/except block,
re-raise it as a CustomError with the original exception as the cause.
Display both the custom error message and the original exception message.
"""

class CustomError(Exception):
    def __str__(self):
        return f"This is a custom error"


class SpecificError(Exception):
    def __str__(self):
        return f"This is a specific error"
    

try:
    number = int(input("Enter a number: "))
    if number > 9:
        raise SpecificError()
except SpecificError as specific_error:
    try:
        raise CustomError() from specific_error
    except CustomError as custom_error:
        print(f'Error: {custom_error}')
        print(f'Original exception: {custom_error.__cause__}')
else:
    print("Cool!")
 