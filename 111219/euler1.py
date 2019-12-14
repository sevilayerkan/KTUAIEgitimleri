#Project Euler #1
#Author : KTU AI Society
#Date : 11.12.19

sum = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        sum +=i
print (sum)

sum2 = 0
for i in range(1,1000):
    if i%3 == 0:
        sum2 += i
    if i%5 == 0:
        sum2 += i
print (sum2)
