#WAP to check whether a given number is paliandrome or not?
#111,121,131,333,434,454,.......

num=int(input("Enter the number: "))

rev=0
temp=num
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if rev==temp:
    print("palindrome")
else:
    print("not palindrome")

