import datetime

today=datetime.date.today()
print(today)

now=datetime.datetime.now()
print(now)

now=datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))

