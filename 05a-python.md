# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>Apart from tuples being immutable there is also a semantic distinction that should guide their usage. Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences. Tuples have structure, lists have order. Tuples are usable as a dictionary keys, while lists are not. If you use list as keys, the approach would be very slow with a large number of items - in complexity terms, this algorithm would be O(n), where n is the number of items in the mapping. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda expression is the anonymous equivalent of a normal function whose
body isa single return statement.You can use a lambda expression wherever you could use a reference
to a function. Here’san example that uses a lambda
expression as an argument to the built-in filter function:
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
high = 7
filter(lambda x, l=low, h=high: h>x>l, aList) # returns: [4, 5, 6]
>>> student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> The simplest form of a list comprehension is [ expression-involving-loop-variable for loop-variable in sequence ]
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

 
Just like set comprehensions, dict comprehensions were added to python in version 2.7. Below we create a mapping of a number to its square using 
dict comprehensions.

>>> x = {i:i**2 for i in range(10)}
>>> x
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
---

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


>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

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

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

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

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





