'''
Create 'list'-like object, but index starts from 1 and index of 0 raises error.
Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи),
але індексація повинна починатись із 1
'''


class CustomList(list):

    @staticmethod
    def value_check(index):
        if index == 0:
            raise IndexError
        elif index is not None and index > 0:
            return index - 1
        else:
            return index

    def __getitem__(self, index):
        if isinstance(index, slice):
            # Handle slicing
            start, stop, step = index.start, index.stop, index.step
            start = self.value_check(start)
            stop = self.value_check(stop)
            return super().__getitem__(slice(start, stop, step))
        else:
            # Handle single integer index
            if index == 0:
                raise IndexError("Index starts from 1")
            return super().__getitem__(index - 1 if index > 0 else index)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError("Index starts from 1")
        super().__setitem__(index - 1, value)

    def __delitem__(self, index):
        if index == 0:
            raise IndexError("Index starts from 1")
        super().__delitem__(index - 1)

my_list = CustomList([1, 2, 3, 4])
print(my_list[1:-1])

