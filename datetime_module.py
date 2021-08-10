# datetime class ka object banana hai to import kr na lounde

from datetime import datetime           # dono ka name same hai
dt1 =datetime(year=2020, month=6, day=30)
dt2 =datetime(year=2020, month=9, day=9, hour=15, minute=19)
dt3 =datetime(2021, 4,28)
dt4 =datetime(2021,3,7,20,30)
print(dt1)
print(dt2)
print(dt3)
print(dt4)
print()
print(dt1.year,dt1.month)       #aur kuchh bhi kr sakte ho bhai
print()

## Now to deal with datetime class 
from datetime import datetime
ct =datetime.now()
print(ct)
print(ct.year)
print(ct.month)
print(ct.hour)
