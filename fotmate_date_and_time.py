# Formatting Date and Time
from datetime import datetime
dt = datetime.today()
print(dt)
print()

newd1 = dt.strftime("%B, %d, %Y")
print(newd1)
print()

new2 = dt.strftime("%d/ %b/ %Y")
print(new2)
print()

new3 =dt.strftime("%d-%m-%Y")
print(new3)
print()

newt1 = dt.strftime("%H:%M:%S")
print(newt1)
print()

newt2 = dt.strftime("%I:%M:%S")
print(newt2)
