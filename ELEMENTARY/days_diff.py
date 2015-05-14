from datetime import date

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    date1, date2 = date(*date1), date(*date2)
    date_diff = (date1 - date2) if date1 > date2 else (date2 - date1)
    return date_diff.days

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238