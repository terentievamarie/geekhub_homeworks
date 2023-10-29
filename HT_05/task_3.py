"""
Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями.
Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї),
пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та
у випадку нервіності - виводити ще і різницю.

    Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      вiдповiдь - "х дорiвнює z"
"""


def value_difference(x, y):
    res = ''
    if x > y:
        res = f"x is more than y by {x - y} "
    elif x < y:
        res = f"y is more than x by {y - x} "
    else:
        res = f"x == y"
    return res

try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(value_difference(x, y))
except ValueError:
    print("x and y must be integer")
 