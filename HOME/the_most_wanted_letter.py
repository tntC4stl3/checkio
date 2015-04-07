#!/usr/bin/env python
# coding: utf-8

import string

def checkio(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in string.letters:
            char_dict[char] = char_dict[char] + 1 if char in char_dict.keys() else 1
    # sort by value Desc then by key Asc
    chars = sorted(char_dict.items(), key=lambda item: (-item[1], item[0]))
    return chars[0][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    assert checkio(u"Fsbd") == "b"
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")