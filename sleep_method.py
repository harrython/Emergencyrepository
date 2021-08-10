#PVM stops program execution for given amount of time

import time

for i in range(2000):
    print(i)
    if(i==10):
        time.sleep(5)
