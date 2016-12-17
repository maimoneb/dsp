from csv import writer

from advanced_python_regex import read_data, get_emails

data = read_data('faculty.csv')

emails = [x[0] for x in get_emails(data)]


with open('emails.csv', 'wb') as csvfile:
    
    email_writer = writer(csvfile)
    
    for email in emails:
        
        email_writer.writerow([email])
