"""
4. Реалізуйте генератор, 
який приймає на вхід будь-яку ітерабельну послідовність 
(рядок, список, кортеж) і повертає генератор, 
який буде вертати значення з цієї послідовності, 
при цьому, якщо було повернено останній елемент із послідовності 
- ітерація починається знову.
Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in generator([1, 2, 3]):
       print(elem)
   1
   2
   3
   1
   2
   3
   1
   .......
"""


def generator(sequence):
    if not isinstance(sequence, (str, list, tuple)):
        raise ValueError("The sequence must be a string, a list or a tuple")
    
    index = 0
    while True:
        yield sequence[index]
        index += 1
        if index == len(sequence):
            index = 0
        

if __name__ == '__main__':
    try:
        for elem in generator([1, 2, 3]):
            print(elem)
    except ValueError as e:
        print(e)
 