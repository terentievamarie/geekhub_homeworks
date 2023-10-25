"""
Create a Python script that takes an age as input. 
If the age is less than 18 or greater than 120, 
raise a custom exception called InvalidAgeError.
Handle the InvalidAgeError by displaying an appropriate error message.
"""


class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
    
    def __str__(self):
        return f"{self.age} is not allowed"


try:
    age_1 = int(input("Please, enter your age: "))
    if age_1 < 18 or age_1 > 120:
        raise InvalidAgeError(age_1)
    print(f"Entered age is {age_1}")
except InvalidAgeError as e:
    print("Entered age is not allowed")
