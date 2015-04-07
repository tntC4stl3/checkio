#!/usr/bin/env python
# coding: utf-8


FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    num_str = []
    # handle hundred
    hundred = number / 100
    if hundred:
        num_str.extend([FIRST_TEN[hundred-1], HUNDRED])
        number %= 100
    # handle rest
    if number < 10 and number > 0:
        num_str.append(FIRST_TEN[number - 1])
    elif number >= 10 and number < 20:
        num_str.append(SECOND_TEN[number - 10])
    elif number >= 20:
        second_ten = number / 10
        number %= 10
        num_str.append(OTHER_TENS[second_ten - 2])
        if number > 0:
            num_str.append(FIRST_TEN[number - 1])
    return ' '.join(num_str)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"