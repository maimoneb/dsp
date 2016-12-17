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
