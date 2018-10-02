def upone(mutable, index):
    mutable[index] = mutable[index].upper()


list_ = ["a", "b", "c"]
upone(list_, 1)
print(list_)  # ['a', 'B', 'c']

dict_ = {"a": "anders", "b": "bengt"}
upone(dict_, "b")
print(dict_)  # {'a': 'anders', 'b': 'BENGT'}
