"""It is an infinite loop
To break a while true loop, break statement is used"""
# n=1
# while True:
#     print(n)
#     n=n+1
#     break
while True:
    num1=int(input("enter a number here :"))
    num2=int(input("entre another number here :"))
    sum=num1+num2
    print(sum)
    repeat=input('do u want to stop the program: ')
    if repeat=="yes":
        break