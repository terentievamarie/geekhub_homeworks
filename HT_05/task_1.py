"""
1. Написати функцiю season, яка приймає один аргумент
(номер мiсяця вiд 1 до 12)
та яка буде повертати пору року, якiй цей мiсяць належить 
(зима, весна, лiто або осiнь).
У випадку некоректного введеного значення 
- виводити відповідне повідомлення.
"""


def season(month):
    try:
        month_number = int(month)
        res = ''
        if month_number == 12 or month_number == 1 or month_number == 2:
            res = "Winter"
        elif month_number >= 3 and month_number <= 5:
            res = "Spring"
        elif month_number >=6 and month_number <= 8:
            res = "Summer"
        elif month_number >= 9 and month_number <= 11:
            res = "Autumn"
        else:
            res = "Incorrect month"
        return res
    except ValueError:
        return "Invalid input"
 
print(season(1))
 