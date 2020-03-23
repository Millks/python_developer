
'''Экземпляр класса'''
from main import *

a = MyArray('i', 2, 3, 6, 8, 1, 6, 8, 3, 6, 6)

'''Пример __getitem__'''
print("__getitem___")
print(a[3])

'''Пример __len__'''
print("__len___")
print(len(a))

'''Пример __contains__'''
print("__contains___")
print(3 in a)
print(10 in a)

'''Итератор пример'''
print("__iter___")

itr = iter(a)
# обход коллекции

while True:
    try:
        print(next(itr))
    except StopIteration:
        break

'''Пример __reversed__'''
print("__reversed___")
itr = reversed(a)
# обход коллекции

while True:
    try:
        print(next(itr))
    except StopIteration:
        break

'''Пример __index__'''
print("__index___")
print("Индекс первого вхождения цифры 6 -", a.index(6))

'''Пример __count__'''
print("__count___")
print("Количесвто вхождений цифры 6 -", a.count(6))
