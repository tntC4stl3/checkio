from string import ascii_lowercase

def check_pangram(text):
    return False if filter(lambda ch: ch not in text.lower(), ascii_lowercase) else True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
