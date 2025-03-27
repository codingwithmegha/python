#WAP to check where the given number is prime or not.
#1 2 3 5 7 11 13 17 19.......
num=int(input("enter the number: "))
if num<=1:
    print("it is not a prime")
else:
 for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")