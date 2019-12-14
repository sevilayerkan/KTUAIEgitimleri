#Project Euler #3
#Author : KTU AI Society
#Date : 11.12.19

def isPrime(sayi):
    for i in range(2,int(sayi**(0.5))):
        if sayi % i == 0:
            return False
    return True

t=600851475143
for i in range(1,t,2):
    if t%i == 0 and isPrime(i):
        print(i)
