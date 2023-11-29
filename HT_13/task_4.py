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
        if index == 0 or index > len(self.data):
            raise IndexError("Index starts from 1")
        return self.data[index - 1]

    def __len__(self):
        return len(self.data) 

    def __repr__(self):
        return repr(self.data)
    

my_list = MyList([10, 20, 30])
print(my_list) 
print(my_list[1])  
print(len(my_list))
 