"""
1. Написати функцiю season, яка приймає один аргумент
(номер мiсяця вiд 1 до 12)
та яка буде повертати пору року, якiй цей мiсяць належить 
(зима, весна, лiто або осiнь).
У випадку некоректного введеного значення 
- виводити відповідне повідомлення.
"""


def season(month_number):
    seasons = {
        'Winter': [12, 1, 2],
        'Spring': [3, 4, 5],
        'Summer': [6, 7, 8],
        'Autumn': [9, 10, 11]
    }

    try:
        month = int(month_number)
        for season_name, months in seasons.items():
            if month in months:
                return f"Season: {season_name}"
    except ValueError:
         return "Invalid input. Enter a valid integer between (1-12)"

print(season(3))
print(season('f'))
 