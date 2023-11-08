"""
6. Напишіть функцію,яка прймає рядок з декількох слів 
і повертає довжину найкоротшого слова. 
Реалізуйте обчислення за допомогою генератора.
"""


def min_word(input_string):
    string_lst = input_string.split()

    if not string_lst:
        return 0
    
    min_word = (min(len(word) for word in string_lst))
    return min_word

if __name__ == '__main__':
    print(min_word('There are cats '))
 