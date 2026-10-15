from datetime import date

year = int(input("year: "))
week = int(input("week: "))

monday = date.fromisocalendar(year, week, 1)

print(monday.ctime())
