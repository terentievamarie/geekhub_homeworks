"""
4. Create 'list'-like object, 
but index starts from 1 and index of 0 raises error. 
Тобто це повинен бути клас, 
який буде поводити себе так, 
як list (маючи основні методи), але індексація повинна починатись із 1
"""


class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        try:
            if isinstance(index, slice):
                start, stop, step = index.start, index.stop, index.step
                start = max(1, start) if start is not None else 1
                stop = max(1, stop) if stop is not None else len(self.data) 
                step = step or 1
                return [self.data[i - 1] for i in range(start, stop, step)]
            if index < 1:
                raise IndexError("Error: Index starts from 1")
            return self.data[index - 1]
        except IndexError as e:
            print(f"Error: {e}")
            
    def __setitem__(self, index, value):
        if index < 1:
            raise IndexError("Index starts from 1")
        self.data[index - 1] = value

    def __delitem__(self, index):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        del self.data[index - 1]

    def append(self, i):
        self.data.append(i)

    def __len__(self):
        return len(self.data) 
    
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.data):
            result = self.data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __repr__(self):
        return repr(self.data)


my_list = MyList([10, 20, 30, 40])
print(my_list)
print(my_list[1]) 
print(my_list[1:3])
print(my_list[1:]) 
print(len(my_list))
for i in my_list:
    print(i * 2)
print(my_list[-1])
 