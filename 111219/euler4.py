#Project Euler #4
#Author : KTU AI Society
#Date : 11.12.19

##Not : Tamamlanacak


def isPalindrome(sayi):
    sayi_str = str(sayi)
    length = int((len(sayi_str)/2)


    for i in range(length):
    	#print(i,length-i)
        if sayi_str[i] != sayi_str[len(sayi_str)-i-1]:
            return False
    return True

print(isPalindrome(9009))
