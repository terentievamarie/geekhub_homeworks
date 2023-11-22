"""
2. Створити клас Person, в якому буде присутнім метод __init__ 
який буде приймати якісь аргументи, які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, 
print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів 
створіть атребут profession (його не має інсувати під час ініціалізації).
"""


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    
    def show_age(self):
        print(f'Age: {self.age}')
    

    def print_name(self):
        print(f'Name: {self.name}')


    def show_all_information(self):
        print(f"Name: {self.name}, surname: {self.surname}, age: {self.age}")
    

person_1 = Person('Bob', 'Black', 30)
person_2 = Person('Mike', "Smith", 33)

person_1.profession = 'Engineer'
person_2.profession = 'English teacher'

print(person_1.profession)
person_2.show_age()
person_1.print_name()
person_2.show_all_information()

 