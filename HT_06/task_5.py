"""
5. Написати функцію <fibonacci>,
яка приймає один аргумент і виводить всі числа Фібоначчі,
що не перевищують його.
"""


def fibonacci(n):
    a, b = 0, 1
    final_list = []
    while a <= n:
        final_list.append(a)
        a, b = b, a + b
    print(final_list)

fibonacci(5)
 