def check(mins, pigeons, food):
    """
    mins: refer to the miniutes
    pigeons: how many pigeons we have at in last round.
    food: tell us how many food we have."""
    print mins, pigeons, food
    if food > pigeons:
        pigeons_next = pigeons + mins + 1
        return check(mins+1, pigeons_next, food-pigeons)
    else:
        pigeons_pre = pigeons - mins
        if food >= pigeons_pre:
            return food
        else:
            return pigeons_pre

def checkio(number):
    return check(1, 1, number)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"