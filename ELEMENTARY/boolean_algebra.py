OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    ret = None
    if operation == OPERATION_NAMES[0]:
        ret = x and y
    elif operation == OPERATION_NAMES[1]:
        ret = x or y
    elif operation == OPERATION_NAMES[2]:
        ret = (not x) or y
    elif operation == OPERATION_NAMES[3]:
        ret = (x or y) and not (x and y)
    elif operation == OPERATION_NAMES[4]:
        ret = not ((x or y) and not (x and y))

    return ret

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"