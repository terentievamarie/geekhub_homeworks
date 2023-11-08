"""
3. Всі ви знаєте таку функцію як <range>.
Напишіть свою реалізацію цієї функції.
Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
P.S. Повинен вертатись генератор.
P.P.P.S Не забудьте обробляти невалідні ситуації
(аналог range(1, 10, )).
Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(*args):
    if not len(args):
        raise ValueError("my_range() takes at least 1 argument")

    if len(args) == 1:
        end = args[0]
        start, step = 0, 1
    elif len(args) == 2:
        start, end = args
        step = 1
    elif len(args) == 3:
        start, end, step = args
    else:
        raise ValueError("my_range() takes at most 3 arguments")

    if step == 0:
        raise ValueError("Step cannot be zero")

    current_value = start
    if start < end:
        if step < 0:
            raise ValueError("Step must be positive there")
        while current_value < end:
            yield current_value
            current_value += step
    elif start > end:
        if step > 0:
            raise ValueError("Step must be negative there")
        while current_value > end:
            yield current_value
            current_value += step
    else:
        return


if __name__ == '__main__':
    try:
        for i in my_range(1, 10, -1):
            print(i)
    except ValueError as e:
        print(e)
 