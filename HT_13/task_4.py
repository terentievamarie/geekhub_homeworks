"""
4. Create 'list'-like object, 
but index starts from 1 and index of 0 raises error. 
Тобто це повинен бути клас, 
який буде поводити себе так, 
як list (маючи основні методи), але індексація повинна починатись із 1
"""


class MyList(list):
    def __getitem__(self, index):
        try:
            if isinstance(index, slice):
                start, stop, step = index.start, index.stop, index.step
                start = max(1, start) if start is not None else 1
                stop = max(1, stop) if stop is not None else len(self) 
                step = step or 1
                return super().__getitem__(slice(start - 1, stop - 1, index.step))
            if index < 1:
                raise IndexError('negative (or zero) index is not allowed. Index starts from 1!')
            return super().__getitem__(index - 1)
        except IndexError as e:
            print(f"Error: {e}")           
    
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
 