"""
4. Create 'list'-like object, 
but index starts from 1 and index of 0 raises error. 
Тобто це повинен бути клас, 
який буде поводити себе так, 
як list (маючи основні методи), але індексація повинна починатись із 1
"""


class MyList(list):
    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]
        
        if index < 1:
            raise IndexError('Negative (or zero) index is not allowed')
        return super().__getitem__(index - 1)
        
    def insert(self, index, value):
        super().insert(index - 1, value)


my_list = MyList([10, 20, 30, 40])
print(my_list)
print(my_list[1]) 
print(my_list[1:3])
print(my_list[1:]) 
print(len(my_list))
for i in my_list:
    print(i * 2)
my_list.pop()
print(my_list)
my_list.append(40)
print(sum(my_list))
my_list.insert(1, 14)
print(my_list)
 