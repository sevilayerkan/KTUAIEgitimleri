#Project Euler #2
#Author : KTU AI Society
#Date : 11.12.19

#Recursif mantik kullanıldığında:

def fib(sayi):
    if sayi != 1 and sayi != 0:
        return fib(sayi -1) + fib(sayi -2)
    else:
        return 1

#print (fib(5))

sum = 0;
i = 0;
while sum < 4000000:
    temp = fib(i) #iki defa hesaplamayı engellemek için
    if temp%2 == 0:
        sum += temp
    i += 1

print (sum)
