import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2022,4))

print(calendar.monthcalendar(2022,4))

print(calendar.calendar(2022))

day_of_the_week=calendar.weekday(2022,4,4)
print(day_of_the_week)

is_aleap_year=calendar.isleap(2022)
print(is_aleap_year)

how_many_leap_days=calendar.leapdays(2020,2030)
print(how_many_leap_days)