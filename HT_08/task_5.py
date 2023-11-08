"""
5. Напишіть функцію,яка приймає на вхід рядок 
та повертає кількість окремих регістро-незалежних букв та цифр, 
які зустрічаються в рядку більше ніж 1 раз. 
Рядок буде складатися лише з цифр та букв (великих і малих). 
Реалізуйте обчислення за допомогою генератора.
Example (input string -> result):
"abcde" -> 0            # немає символів, що повторюються
"aabbcde" -> 2          # 'a' та 'b'
"aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
"indivisibility" -> 1   # 'i' присутнє 6 разів
"Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
"aA11" -> 2             # 'a' і '1'
"ABBA" -> 2             # 'A' і 'B' кожна двічі
"""


def quantity(input_string):
    input_string = input_string.lower()
    symbol_count = {}

    for char in input_string:
        if char.isalnum():
            if char in symbol_count:
                symbol_count[char] += 1
            else:
                symbol_count[char] = 1

    for char, count in symbol_count.items():
        if count > 1:
            yield char, count


def result_sum(input_string):
    return sum(1 for char, count in quantity(input_string))


if __name__ == '__main__':
    print(result_sum('aA11'))
 