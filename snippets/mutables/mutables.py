def upone(mutable, index):
    mutable[index] = mutable[index].upper()


list = ['a', 'b', 'c']
upone(list, 1)
print list  # ['a', 'B', 'c']

dict = {'a': 'anders', 'b': 'bengt'}
upone(dict, 'b')
print dict  # {'a': 'anders', 'b': 'BENGT'}
