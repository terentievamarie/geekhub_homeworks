"""
9. Користувачем вводиться початковий і кінцевий рік.
Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно). 
P.S. Рік є високосним, якщо він кратний 4, але не кратний 100,
а також якщо він кратний 400.
"""

start_year = int(input("Please enter the start year: "))
end_year = int(input("Please enter the end year: "))

for i in range(start_year, end_year + 1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i)