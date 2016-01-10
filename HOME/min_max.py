def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = list(args[0])
    items = args[::] if key is None else map(key, args)
    min_index = 0
    for i in range(1, len(items)):
        if items[min_index] > items[i]:
            min_index = i
    return args[min_index]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = list(args[0])
    items = args[::] if key is None else map(key, args)
    max_index = 0
    for i in range(1, len(items)):
        if items[max_index] < items[i]:
            max_index = i
    return args[max_index]



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
