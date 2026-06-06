# import time as clock
# x=clock.localtime(clock.time())
# print(x)

# import time as tm
# b=tm.asctime(tm.localtime(tm.time()))
# print(b)

# # Wed Oct 15 10:51:30 2025...DDTY

# print("hello codegnan")
# print("hello codegnan")
# print("hello codegnan")
# tm.sleep(3)
# print("hello codegnan")

# #stringparsetime... strptime
# from datetime import datetime
# a="12-6-2023 6:35:52"
# b=datetime.strptime(a,"%d-%m-%Y %H:%M:%S")
# print(b)

# #strftime...string format time
# from datetime import datetime 
# a=datetime.now()
# b=a.strftime("%d-%m-%y %H:%M:%S %d-%m-%y")
# print(b)

from datetime import date
x=date.today()
print(x)
print(x.month)
print(x.year)
print(x.day)
print(x.weekday()) # monday starts with 0
print(x.isoweekday()) #for this output is based on below format
# 1: Monday
# 2: Tuesday
# 3: Wednesday
# 4: Thursday
# 5: Friday
# 6: Saturday
# 7: Sunday 

