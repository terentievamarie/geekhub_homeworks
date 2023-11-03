"""
1. Створіть функцію, всередині якої будуть записано список 
із п'яти користувачів 
(ім'я та пароль). Функція повинна приймати три аргументи: 
два - обов'язкових (<username> та <password>) і 
третій - необов'язковий параметр <silent> 
(значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
    якщо silent == True - функція вертає False
    якщо silent == False -породжується виключення LoginException 
    (його також треба створити =))
"""


class LogicException(Exception):
    def __str__(self):
        return "Logic Exception"


def does_user_exist(username, password, silent=False):
    if not username or not password:
        return False
    
    users_list = [
        ('Alex', '1234'),
        ('Alina', '1244'),
        ('Alibek', '13644'),
        ('Angelina', '3544'),
        ('Almaz', '20244')
    ]
    
    for user, pwd in users_list:
        if username == user and password == pwd:
            return True

    if not silent:
        raise LogicException()
    
    return False

if __name__ == '__main__':
    try:
        print(does_user_exist('Alex', '234'))
    except LogicException as e:
        print(e)
 