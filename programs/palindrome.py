import re

def remove_punctuation(value):
    return re.sub('\W+', '', value)

def isPalindrome(value):
    # return remove_punctuation(value.lower()) == remove_punctuation(value[::-1].lower())      # using slice slice[start:stop:step]  -1 indicates last element
    return remove_punctuation(value.lower()) == remove_punctuation(''.join(reversed(value)).lower())   # reversed used to reverse both mutable and immutable objects

def main():
    assert isPalindrome('malayalam')
    assert not isPalindrome('malayalama')
    assert isPalindrome('m#ala yal!a@m$')
    assert isPalindrome('Malayalam')

if __name__ == '__main__':
    main()