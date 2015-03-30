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

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
