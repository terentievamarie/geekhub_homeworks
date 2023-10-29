"""
4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe 
kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
-> просто потицяв по клавi =)
Створіть ф-цiю, яка буде отримувати рядки на зразок цього
та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно)
     -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 
    -> прiнтує суму всiх чисел та окремо рядок без цифр 
    лише з буквами (без пробілів)
-  якщо довжина більше 50
    -> щось вигадайте самі, проявіть фантазію =)
"""


def parse_string(input_string):
    numbers = [int(i) for i in input_string if i.isdigit()]
    letters = [i for i in input_string if i.isalpha()]
    if len(input_string) >= 30 and len(input_string) <= 50:
        print(len(input_string), len(letters), len(numbers))
    elif len(input_string) <= 30:
        print(sum(numbers), ''.join(letters))
    else:
        res = ''.join(letters) + ''.join(str(num) for num in numbers)
        print(res[::-1])

parse_string("i234love4464python3334fregergergergergergergergregerge")
 