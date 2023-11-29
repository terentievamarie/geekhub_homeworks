"""
3. Створіть клас в якому буде атрибут 
який буде рахувати кількість створених екземплярів класів.
"""


class MyClass:
    counter = 0

    def __init__(self, name):
        self.name = name
        MyClass.counter += 1


person_1 = MyClass('Masha')
print(person_1.counter)

person_2 = MyClass('Anna')
print(person_2.counter)

person_3 = MyClass('Inna')
print(person_3.counter)
 