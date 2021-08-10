# date ko aage barhata hai ya piche karta hai    expiry date set karne k kam aata hai

from datetime import timedelta, date
td = timedelta(days=10)
d = date.today()            # aaj ka date 10 din aage hai leke jana
print(d+td)
