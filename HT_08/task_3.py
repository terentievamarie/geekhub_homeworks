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
(аналог range(1, -10, 5)).
Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(start=0, stop=None, step=1):
    if step == 0:
        raise ValueError("Step cannot be zero")
    
    if stop is None:
        stop = start
        start = 0

    if (start >= stop and step > 0) or (start <= stop and step < 0):
        return iter(())

    current = start

    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step


if __name__ == '__main__':
    try:
        for i in my_range(1, -10, 5):
            print(i)
    except ValueError as e:
        print(e)
 