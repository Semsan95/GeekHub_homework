'''
Create 'list'-like object, but index starts from 1 and index of 0 raises error.
Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи),
але індексація повинна починатись із 1
'''


class NewList:

    def __init__(self, *args):
        self.elements = list(args)

    @staticmethod
    def _zero_check(index):
        if index == 0:
            raise IndexError('Індексація починається з 1')

    def __getitem__(self, index):
        self._zero_check(index)
        new_index = index % len(self.elements)
        if index > 0:
            return self.elements[new_index - 1]
        else:
            return self.elements[new_index]

    def __setitem__(self, index, value):
        self._zero_check(index)
        self.elements[index - 1] = value

    def __delitem__(self, index):
        self._zero_check(index)
        del self.elements[index - 1]

    def __repr__(self):
        return repr(self.elements)

my_list = NewList(1, 2, 3)
print(my_list[-1])

