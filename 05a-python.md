# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Apart from tuples being immutable there is also a semantic distinction that should guide their usage. Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences. Tuples have structure, lists have order. Tuples are usable as a dictionary keys, while lists are not. If you use list as keys, the approach would be very slow with a large number of items - in complexity terms, this algorithm would be O(n), where n is the number of items in the mapping. 


###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets can't contain duplicates. Sets are unordered. In order to find an element in a set, a hash lookup is used (which is why sets are unordered). This makes __contains__ (in operator) a lot more efficient for sets than lists.
Sets can only contain hashable items (see #3). If you try: set(([1],[2])) you'll get a TypeError.
In practical applications, lists are very nice to sort and have order while sets are nice to use when you don't want duplicates and don't care about order.

Also, list can be 2-D whereas a set can't. 2) As list are ordered (IE. have serial number) list are comparatively slow to execute whereas sets are fast. 3) List in python is like Array of java or c. 4) Printing a set almost always provide different sequence of output.


###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

A lambda expression is the anonymous equivalent of a normal function whose
body isa single return statement.You can use a lambda expression wherever you could use a reference
to a function. Here’san example that uses a lambda
expression as an argument to the built-in filter function:
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
high = 7
filter(lambda x, l=low, h=high: h>x>l, aList) # returns: [4, 5, 6]
         student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

The simplest form of a list comprehension is [ expression-involving-loop-variable for loop-variable in sequence ]
This will step over every element of sequence, successively setting loop-variable equal to every element one at a time, and will then build up a list by evaluating expression-involving-loop-variable for each one. This eliminates the need to use lambda forms, and thus generally produces a much more readable code than using map() and a more compact code than using a for-loop.

The first example <first-example-list-comprehension> can thus be written compactly as:

>>> squares = [ x**2 for x in range(10) ]
>>> print squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

The map() function applies a function to every member of an iterable (seq) and returns the result. Typically, one would use an anonymous inline function as defined by lambda, but it is possible to use any function. The first example above can also be accomplished using map() as follows:

>>> def square(x):
...     return x**2
...
>>> squares = map(square, range(10))
>>> print squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

The filter function constructs a list from those elements of seq for which func istrue.
func can be any callable object that accepts a single argument or
None. seq can be any iterable object. When func is callable, filter
calls func on each item of seq and returns the list of items for which
func’s result is true, just like the following string comprehension:
[item for item in seq if func(item)]
When seq is a string or tuple, filter’s result is also a string or tuple
rather than a list. When func is None, filter tests for true items,
just like: [item for item in seq if item]

map may be microscopically faster in some cases (when you're NOT making a lambda for the purpose, 
but using the same function in map and a listcomp). List comprehensions may be faster in other 
cases and most (not all) pythonistas consider them more direct and clearer.

Find list comprehension much clearer than the filter+lambda, but can use whichever you find easier.

There are two things that may slow down your use of filter.

The first is the function call overhead: as soon as you use a Python function (whether created by def or lambda) it is likely that filter will be slower than the list comprehension. It almost certainly is not enough to matter, and you shouldn't think much about performance until you've timed your code and found it to be a bottleneck, but the difference will be there.

The other overhead that might apply is that the lambda is being forced to access a scoped variable (value). That is slower than accessing a local variable and in Python 2.x the list comprehension only accesses local variables. If you are using Python 3.x the list comprehension runs in a separate function so it will also be accessing value through a closure and this difference won't apply.

The other option to consider is to use a generator instead of a list comprehension:

def filterbyvalue(seq, value):
   for el in seq:
       if el.attribute==value: yield el
Then in your main code (which is where readability really matters) you've replaced both list comprehension and filter with a hopefully meaningful function name.


In set comprehensions, we use the braces rather than
square brackets. For example, to create the set of the squares of all numbers between 0 and 10 the following set comprehensions can be used in lieu of regular looping:

>>> x = {i**2 for i in range(10)}
>>> x
set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])
>>> 
 

Just like set comprehensions, dict comprehensions were added to python in version 2.7. Below we create a mapping of a number to its square using 
dict comprehensions.

>>> x = {i:i**2 for i in range(10)}
>>> x
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

 
###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

from datetime import datetime, timedelta
import time

stop = datetime(2015, 07, 28, 0, 0)
start =  datetime(2013, 01, 2, 0, 0)

print stop - start

937 days


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
from datetime import datetime, timedelta
import time

s = "05282015"
s1 = '12312013'

stop2 = datetime(year=int(s[4:8]), month=int(s[0:2]), day=int(s[2:4]))
print stop2

start2 = datetime(year=int(s1[4:8]), month=int(s1[0:2]), day=int(s1[2:4]))

print stop2 - start2

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
from datetime import datetime, timedelta
import time

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

stop3 = datetime.strptime(date_stop,'%d-%b-%Y').date()

start3 = datetime.strptime(date_start,'%d-%b-%Y').date()

print stop3 - start3

7850 days

# Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
### Edit the 7 functions in [q6_strings.py](python/q6_strings.py)


def donuts(count):
    
<!--     Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count. -->

    if count > 9:
        count = 'many'
    else:
        count = str(count)
    return 'Number of donuts: {}'.format(count)


def both_ends(s):
    
<!--     Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
     -->
    if len(s) < 2:
        return ""
    else:
        return s[0:2] + s[-2:]


def fix_start(s):

<!--   Given a string s, return a string where all occurences of its
    first char have been changed to *, except do not change the
    first char itself. e.g. babble yields ba**le Assume that the
    string is length 1 or more. -->
 
    char = s[0]

    s = s[1:].replace(char, '*')
    return  char + s


def mix_up(a, b):
   
<!--     Given strings a and b, return a single string with a and b
    separated by a space <a> <b>, except swap the first 2 chars of
    each string. Assume a and b are length 2 or more. -->

    new_a = b[0:2] + a[2:]
    new_b = a[0:2] + b[2:]
    return '<{}> <{}>'.format(new_a, new_b)


def verbing(s):
  
<!--     Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string. -->

    length = len(s)

    if length > 2:
        if s.endswith('ing'):
            s += 'ly'
        else:
            s += 'ing'
    return s


def not_bad(s):
    
<!--     Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good! -->

    snot = s.find('not')
    sbad = s.find('bad')

    if sbad > snot:
        s = s.replace(s[snot:(sbad + 3)], 'good')

    return s


def front_back(a, b):
   
<!--     Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back -->
    
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

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

import re

def read_data(file_name):
    with open(file_name, 'rb') as inputfile:
        data = inputfile.read()
    return data


def find_unique(regex, data):
    results = [x[0] for x in re.findall(regex, data)]
    return {x : results.count(x) for x in results}


def print_unique(name, d):
    print 'There are ', len(d),' unique ', name, '.'
    print 'Frequencies are:'
    for k, f in d.iteritems():
        print k, ':', f


def print_sequence(s):
    for x in s:
        print x


def get_emails(data):
    return re.findall(r'([\w.-]+@([\w.-]+))', data)


def main():

    data = read_data('faculty.csv')

    # Q1

    print_unique('degrees', find_unique(r'\b([A-Z]+[a-z]*([A-Z]|([.][A-Z]+)+))', data))

    # Q2

    print_unique('titles', find_unique(r'(\b([A-Z][a-z]* )*Professor)', data))

    # Q3

    emails = get_emails(data)
    print 'Emails:'
    print_sequence([x[0] for x in emails])

    # Q4

    unique_domains = set([x[1] for x in emails])
    print 'There are ', len(unique_domains), ' unique email domains.'
    print 'They are:'
    print_sequence(unique_domains)


if __name__ == "__main__":
    main()


##Q8. Parsing
## Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)

###The football.csv file contains the results from the English Premier League.
 ###The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
 ###goals scored for and against each team in that season (so Arsenal scored 79 goals
 ###against opponents, and had 36 goals scored against them). Write a program to read the file,
 ###then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
 


