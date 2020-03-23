from array import array


class MyArray:
    def __init__(self, element_type, *elements):
        self.el_type = element_type
        self.items = array(element_type, elements)

    def __getitem__(self, key):
        return self.items[key]

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return MyIterator(self.items, -1)

    def __reversed__(self):
        return MyIterator(self.items, len(self), -1)

    def index(self, it):
        for i in range(len(self.items)):
            if it == self.items[i]:
                return i

    def count(self, it):
        k = 0
        for i in range(len(self.items)):
            if it == self.items[i]:
                k += 1
        return k


class MyIterator():
    def __iter__(self):
        return self

    def __init__(self, collection, cursor, way=1):
        self._collection = collection
        self._cursor = cursor
        self._way = way

    def __next__(self):
        if self._way > 0:
            if self._cursor + self._way >= len(self._collection):
                raise StopIteration()
            self._cursor += self._way
            return self._collection[self._cursor]
        else:
            if self._cursor + self._way < 0:
                raise StopIteration()
            self._cursor += self._way
            return self._collection[self._cursor]




