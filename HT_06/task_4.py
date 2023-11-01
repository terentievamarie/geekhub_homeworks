"""
4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - 
початок і кінець діапазона, і вертатиме список простих чисел
всередині цього діапазона. 
Не забудьте про перевірку на валідність введених даних 
та у випадку невідповідності - виведіть повідомлення.
"""


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_list(start, end):
    final_list = []
    for i in range(start, end + 1):
        if is_prime(i):
            final_list.append(i)
    return final_list


try:
    start_number = int(input("Please, enter a start number: "))
    end_number = int(input("Please, enter an end number: "))
except ValueError:
    print("Incorrect value")
else:
    print(prime_list(start_number, end_number))
 