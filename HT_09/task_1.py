"""
1. Програма-світлофор.
Створити програму-емулятор світлофора для авто і пішоходів. 
Після запуска програми на екран виводиться в лівій половині 
- колір автомобільного, а в правій - пішохідного світлофора. 
Кожну 1 секунду виводиться поточні кольори. 
Через декілька ітерацій - відбувається зміна кольорів 
- логіка така сама як і в звичайних світлофорах 
(пішоходам зелений тільки коли автомобілям червоний).
Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""
import time


def traffic_lights():
    colors_lst = []

    for _ in range(4):
        colors_lst.append('Red        Green')

    for _ in range(2):
        colors_lst.append('Yellow     Red')

    for _ in range(4):
        colors_lst.append('Green      Red')
    
    for _ in range(2):
        colors_lst.append('Yellow     Red')
    
    i = 0
    while i < len(colors_lst):
        yield colors_lst[i]
        i += 1
        if i == len(colors_lst):
            i = 0


for lights in traffic_lights():
    print(lights)
    time.sleep(1)
 