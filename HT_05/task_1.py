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
        if 1 <= month <= 12:
            for season_name, months in seasons.items():
                if month in months:
                    return f"Season: {season_name}"
            return "Invalid input"
    except ValueError:
        return "Invalid input"

print(season(12))
print(season('f'))
 