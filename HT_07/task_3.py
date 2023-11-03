"""
3. На основі попередньої функції (скопіюйте кусок коду) 
створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів 
   (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, 
   користуючись валідатором, перевірить ці дані і 
   надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
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


def print_user(users_list):
    for user in users_list:
        print(f"Name: {user[0]}")
        print(f"Password: {user[1]}")
        print("Status: ", end='')
        try:
            if func(user[0], user[1]):
                print('OK')
        except CustomException as e:
            print(e)
        finally:
            print("-----")


if __name__ == '__main__':
    users_list = [
            ('Al', '1234'),
            ('Alina', 'fjkdjhgodigj'),
            ('Alibek', '1364488888'),
            ('Angelina', '3544kkkskks'),
            ('alla', '2244uururu')
        ]
    
    print_user(users_list)
 