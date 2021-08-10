
from datetime import datetime
dt = datetime(year=2020, month=6, day=30)
print(dt)
print()

ct = datetime.now()
print(ct)
print()

print(ct.day)
print(ct.month)
print(ct.year)
print()

# if we wanna today instead now()
ct = datetime.today()
print(ct)
print(ct.hour)
