# # # take an input from a user as a string then reverse it.
# # #while True:
a=input("enter the string :")
b=a[::-1]
print("Reverse of string",a,"is :",b)

# #WAP to check if a string contains only digit
a=input("enter the data :")
b=a.isdigit()
if b==True:
 print("contains only digit")
else:
    print("not conatin")

# # #WAP to check whether a string is palindrome or not.
# # #121,323,....
number=input("enter the number: ")
b=number[::-1]
if number==b:
    print("palindrome")
else:
    print("not palindrome")

# #WAP to find number of vowels in the string
a=input("enter the string ")
vowels=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowels=vowels+1
print("total number of vowels :",vowels)

# WAP to check if every word in a string is begin with capital letter.
x=input("enter the string: ")
y=x.istitle()
if y==True:
    print("Stirng is begin with capital letter")
else:
    print("not begin with capital letter")



