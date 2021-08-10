from time import time, ctime, localtime
epoch = time()
print(epoch)

et = ctime(epoch)
print(et)

stobj = localtime()
print(stobj)        #sare attribute dikhayega
print()

print("Year:", stobj.tm_year)
print("Month:", stobj.tm_mon)
print("Date:", stobj.tm_mday)
print("Hour:", stobj.tm_hour)
print("Minute:", stobj.tm_min)
print("Second:", stobj.tm_sec)
print()
print(stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print("stobj.tm_sec")           # sabse jyada use hota hai localtime
