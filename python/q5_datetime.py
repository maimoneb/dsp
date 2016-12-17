 
# Hint:  use Google to find python function

from datetime import datetime, timedelta


stop = datetime(2015, 07, 28, 0, 0)

start =  datetime(2013, 01, 2, 0, 0)

print stop - start


s = "05282015"
s1 = '12312013'

stop2 = datetime(year=int(s[4:8]), month=int(s[0:2]), day=int(s[2:4]))

print stop2

start2 = datetime(year=int(s1[4:8]), month=int(s1[0:2]), day=int(s1[2:4]))

print stop2 - start2

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

stop3 = datetime.strptime(date_stop,'%d-%b-%Y').date()

start3 = datetime.strptime(date_start,'%d-%b-%Y').date()

print stop3 - start3



