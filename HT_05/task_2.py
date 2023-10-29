"""
2. Створiть 3 рiзних функцiї (на ваш вибiр).
Кожна з цих функцiй повинна повертати якийсь результат
(напр. інпут від юзера, результат математичної операції тощо).
Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,
обробляє їх результат та також повертає результат своєї роботи.
Таким чином ми будемо викликати одну (четверту) функцiю,
а вона в своєму тiлi - ще 3.
"""
import random
import sys


def func_1(name):
    return sys.getsizeof(name)


def func_2(surname, birth):
    password = surname + birth
    return password[::-1]


def func_3():
    number_id = random.randint(1, 10)
    return number_id


def func_4():
    memory_space = func_1("Bob")
    password = func_2("Baker", "1992")
    number_id = func_3()
    return (
        "Everything about you in our database.\n"
        f"Your name takes up {memory_space} memory space.\n"
        f"Generated password: {password}\n"
        f"Your number id: {number_id}"
    )

print(func_4())
 