# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

from datetime import datetime
import time

print datetime.today()

stop = datetime(2015, 07, 28, 0, 0)
start =  datetime(2013, 01, 2, 0, 0)

print stop - start

937 days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

from datetime import datetime
import time
s = "05282015"
s1 = '12312013'

stop2 = datetime(year=int(s[4:8]), month=int(s[0:2]), day=int(s[2:4]))
print stop2

start2 = datetime(year=int(s1[4:8]), month=int(s1[0:2]), day=int(s1[2:4]))

print stop2 - start2

513 days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

stop3 = datetime.strptime(date_stop,'%d-%b-%Y').date()

start3 = datetime.strptime(date_start,'%d-%b-%Y').date()

print stop3 - start3

7850 days


