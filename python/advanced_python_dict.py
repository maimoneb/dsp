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
