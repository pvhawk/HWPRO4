class FlatIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.len = len(self.lst)
        self.cursor = 0
        self.cursor2 = 0
        return self

    def __next__(self):
        if self.cursor2 >= len(self.lst[self.cursor]):
            self.cursor += 1
            self.cursor2 = 0

        if self.cursor < self.len:
            self.data = self.lst[self.cursor][self.cursor2]
            self.cursor2 += 1
        else:
            raise StopIteration
        return self.data

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
]
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)