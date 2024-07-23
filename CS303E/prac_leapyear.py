
#year = int(input())

#for x in range(0,10):
    #if year%400 == 0:
     #   print(year)
   # elif year%4 == 0 and year%100 != 0:
    #    print(year)
    #year = year + 1

total = int()
money = float(input())
month = int(input())

for x in range(0,month):
    total = (money+total)*(1.02)
    

print("${:.2f}".format(total))
