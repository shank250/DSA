n=10
week = n//7
daysRem = n%7
money = 0
# if week != 0:
#     money = week*28 + daysRem
#     # money = daysRem*(daysRem+1)//2  
# money = money +  (daysRem*daysRem + daysRem) // 2
weekSum = 28*week

extraWeek= (7*week*week - 7*week)//2
wl = [1,2,3,4,5,6,7]
lastWeek = sum(wl[:daysRem]) + daysRem*week
money = weekSum + extraWeek + lastWeek
print(money)
print(week, daysRem)
print(weekSum, extraWeek, lastWeek)