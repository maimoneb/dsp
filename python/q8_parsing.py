# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

from csv import reader

with open('football.csv', 'rb') as csvfile:

    csv_reader = reader(csvfile, delimiter=',')
    
    header = next(csv_reader)             # skip first(header) row

    data = [row for row in csv_reader]
    

def min_score_difference(data, goals_index, goals_allowed_index):

    goals = [x[goals_index] for x in data]

    goals_allowed = [x[goals_allowed_index] for x in data]

    differences = [int(x) - int(y) for x, y in zip(goals, goals_allowed)]
    
    minimum, min_index = min((val, index) for (index, val) in enumerate(differences))
    
    return min_index

goals_index = header.index('Goals')

goals_allowed_index = header.index('Goals Allowed')

team_name_index = header.index('Team')

result_index = min_score_difference(data, goals_index, goals_allowed_index)

print data[result_index][team_name_index]
