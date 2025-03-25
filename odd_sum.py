# WAP to find sum of first 10 odd numbers using while loop.
i=1
sum=0
while i<=20:
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)
