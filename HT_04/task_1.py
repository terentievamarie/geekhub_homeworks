"""
Написати скрипт, який приймає від користувача два числа (int або float)
і робить наступне: Кожне введене значення спочатку пробує перевести в int.
У разі помилки - пробує перевести в float, а якщо і там ловить помилку -
пропонує ввести значення ще раз (зручніше на даному етапі навчання для
цього використати цикл while)
Виводить результат ділення першого на друге. Якщо при цьому виникає помилка -
оброблює її і виводить відповідне повідомлення
"""

while True:
    number_1 = input("Please, enter a number: ")
    number_2 = input("Please, enter a number: ")
    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
        result = number_1 / number_2
    except ValueError:
        try:
            number_1 = float(number_1)
            number_2 = float(number_2)
            result = number_1 / number_2
        except ValueError:
            print("Incorrect type. Try again.")
        except ZeroDivisionError as e:
            print(e)
        else:
            print(result)
            break
    except ZeroDivisionError as e:
        print(e)
    except Exception as error:
        print(f"Error: {error}")
    else:
        print(result)
        break
