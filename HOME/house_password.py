import re

def checkio(data):

    #replace this for solution
    is_secure = False
    if len(data) >= 10:
        if re.search('[a-z]', data) and \
           re.search('[A-Z]', data) and \
           re.search('[0-9]', data):
            is_secure = True
    return is_secure

# the highest vote answer
# http://www.checkio.org/mission/house-password/publications/oduvan/python-27/first/?ordering=most_voted
def checkio_highest_vote(data):
    return bool(len(data) >= 10 \
        # filter(function, iterable) is equivalent to [item for item in iterable if function(item)]
        and filter(lambda a:a.isupper(), data) \
        and filter(lambda a:a.islower(), data) \
        and filter(lambda a:a.isdigit(), data))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
