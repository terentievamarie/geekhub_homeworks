"""
2. Створіть функцію для валідації пари ім'я/пароль 
за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і 
   повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - 
   породити виключення із відповідним текстом.
"""


class CustomException(Exception):
    pass


def func(name, password):
    if not name or not password:
        raise CustomException("You must enter a name and a password.")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    if len(name) < 3 or len(name) > 50:
        raise CustomException("The name should be between 3 and 50 characters.")
    
    if len(password) < 8:
        raise CustomException("The password must be at least 8 characters long.")
    
    if not any(char.isdigit() for char in password):
        raise CustomException("The password does not contain any digits")
    
    if name == name[::-1]:
        raise CustomException("The string cannot be a palindrome.")
    
    return "This user passed the validation."


if __name__ == '__main__':
    try:
        print(func('Maria', 'jjfsij1sgmpsg'))
    except CustomException as e:
        print(e)
 