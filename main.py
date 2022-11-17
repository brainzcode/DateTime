import datetime as dat

now = dat.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(month)

date_of_birth = dat.datetime(year=1990, month=7, day=11)
print(date_of_birth)
