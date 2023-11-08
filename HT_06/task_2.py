"""
2. Написати функцію <bank> , 
яка працює за наступною логікою: 
користувач робить вклад у розмірі <a> одиниць строком на <years> років 
під <percents> відсотків (кожен рік сума вкладу збільшується 
на цей відсоток,ці гроші додаються до суми вкладу 
і в наступному році на них також нараховуються відсотки).
Параметр <percents> є необов'язковим і має значення
по замовчуванню <10> (10%). 
Функція повинна принтануть суму, яка буде на рахунку,
а також її повернути (але округлену до копійок).
"""


def bank(a, years, percents=10):
    sum = a
    for i in range(years):
        sum += (sum * percents) / 100
    final_sum = round(sum, 2)
    print(final_sum)
    return final_sum

print(bank(1000, 3, 20))
 