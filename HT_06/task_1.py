"""
1. Написати функцію <square>, яка прийматиме один аргумент
- сторону квадрата,
і вертатиме 3 значення у вигляді кортежа: периметр квадрата,
площа квадрата та його діагональ.
"""
import math


def square(side_length):
    perimeter = side_length * 4
    square = side_length ** 2
    diagonal = side_length * math.sqrt(2)
    return (perimeter, square, diagonal)

print(square(5))
 