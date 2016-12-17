
def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count."""

    if count > 9:

        count = 'many'

    else:

        count = str(count)

    return 'Number of donuts: {}'.format(count)


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string."""
    if len(s) < 2:

        return ""

    else:

        return s[0:2] + s[-2:]


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more."""

    char = s[0]

    s = s[1:].replace(char, '*')

    return  char + s


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more."""

    new_a = b[0:2] + a[2:]

    new_b = a[0:2] + b[2:]

    return '<{}> <{}>'.format(new_a, new_b)


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string."""

    length = len(s)

    if length > 2:

        if s.endswith('ing'):

            s += 'ly'

        else:

            s += 'ing'

    return s


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!"""

    snot = s.find('not')

    sbad = s.find('bad')

    if sbad > snot:

        s = s.replace(s[snot:(sbad + 3)], 'good')

    return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back"""

    a_idx = len(a) - (len(a) / 2)

    b_idx = len(b) - (len(b) / 2)

    return a[:a_idx] + b[:b_idx] + a[a_idx:] + b[b_idx:]


def main():
    count = 10
    numdonuts = donuts(count)
    print(donuts(4), 'Number of donuts: 4')

    print(donuts(9), 'Number of donuts: 9')

    print(donuts(10), 'Number of donuts: many')

    print(donuts(99), 'Number of donuts: many')

    print(both_ends('spring'), 'spng')

    print(both_ends('Hello'), 'Helo')

    print(both_ends('a'), '')

    print(both_ends('xyz'), 'xyyz')


    print(fix_start('babble'))

    print(fix_start('aardvark'))

    print(fix_start('google'))

    print(fix_start('donut'))

    print fix_start('babble')

    print(mix_up('mix', 'pod'))

    print(mix_up('dog', 'dinner'))

    print(mix_up('gnash', 'sport'))

    print(mix_up('pezzy', 'firm'))

    print(verbing('hail'))

    print(verbing('swiming'))

    print(verbing('do'))

    print(not_bad('This movie is not so bad'), 'This movie is good')

    print(not_bad('This dinner is not that bad!'), 'This dinner is good!')

    print(not_bad('This tea is not hot'), 'This tea is not hot')

    print(not_bad("It's bad yet not"), "It's bad yet not")

    print(front_back('abcd', 'xy'), 'abxcdy')

    print(front_back('abcde', 'xyz'), 'abcxydez')

    print(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == "__main__":

    main()
