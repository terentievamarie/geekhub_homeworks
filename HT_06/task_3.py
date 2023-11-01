"""
3. Написати функцию <is_prime>, яка прийматиме 1 аргумент -
число від 0 до 1000, и яка вертатиме True,
якщо це число просте і False - якщо ні.
"""


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
    

try:
    number = int(input("Enter a number: "))
    if number < 0 or number > 1000:
        print("Number must be from 0 to 1000")
except ValueError:
    print("Incorrect value")
else:
    print(is_prime(number))
 