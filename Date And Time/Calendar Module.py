# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month,day,year=list(map(int, input().split()))

def guess_day(month,day,year):
    weekday=calendar.weekday(year,month,day)
    weekday_cap=calendar.day_name[weekday].upper()
    return weekday_cap
    
result= guess_day(month,day,year)
print(result)
