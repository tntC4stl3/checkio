#!/usr/bin/env python
# coding: utf-8


def checkio(game_result):
    all_lines = []
    # rows
    all_lines.extend([list(row) for row in game_result])
    # cols
    for i in range(3):
        line = []
        for j in range(3):
            line.append(game_result[j][i])
        all_lines.append(line)
    # diagnol
    all_lines.append([game_result[0][0], game_result[1][1], game_result[2][2]])
    all_lines.append([game_result[0][2], game_result[1][1], game_result[2][0]])

    for line in all_lines:
        if line[0] == line[1] == line[2]:
            if line[0] == 'X':
                return 'X'
            elif line[0] == 'O':
                return 'O'
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"



