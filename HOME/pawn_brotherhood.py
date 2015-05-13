def safe_pawns(pawns):
    count = 0
    for pawn in pawns:
        column = pawn[0]
        row = pawn[1]
        brother_columns = (chr(ord(column)-1), chr(ord(column)+1))
        brother_row = int(row) - 1
        for brother_column in brother_columns:
            brother_pawn = '%s%d' % (brother_column, brother_row)
            if brother_pawn in pawns:
                count += 1
                break
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1