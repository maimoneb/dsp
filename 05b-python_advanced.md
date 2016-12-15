## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  

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



####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> See module above

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> See module above


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> See module above

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> See module above

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

>> See module above


###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

from csv import writer
from advanced_python_regex import read_data, get_emails

# Q5-

data = read_data('faculty.csv')
emails = [x[0] for x in get_emails(data)]

with open('emails.csv', 'wb') as csvfile:
    email_writer = writer(csvfile)
    for email in emails:
        email_writer.writerow([email])

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

import csv, re
from collections import defaultdict


def trim_strings(csv_reader):
    return [[x.strip() for x in row] for row in csv_reader]


def print_dictionary(d, num_elements):
    for i in range(0, num_elements):
        print d.keys()[i], ':', d.values()[i]

with open('faculty.csv', 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader) # ignore header row
    data = trim_strings(csv_reader)

# Q6

only_lastname = lambda name: re.search(r'\b([A-Za-z]+)$', name).group(1)

dictionary1 = defaultdict(list)
for row in data:
    dictionary1[only_lastname(row[0])].append(row[1:])

print("Dictionary 1:")
print_dictionary(dictionary1, 3)

# Q7

print("Dictionary 2:")
dictionary2 = {tuple(row[0].split(' ')) : row[1:] for row in data}
print_dictionary(dictionary2, 3)

# Q8

print("Sorted dictionary 2:")
for key in sorted(dictionary2.keys(), key=lambda x: x[-1]):
    print key, ':', dictionary2[key]

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> See above module

####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> See above module

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

