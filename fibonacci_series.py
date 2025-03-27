# WAP to get Fibonacci series upto 10 numbers
# 0 1 1 2 3 5 8 13......

firstelement = 0
secondelement = 1
print(firstelement)
print(secondelement)
for i in range(1,10):
    thirdelement=firstelement+secondelement
    firstelement=secondelement
    secondelement=thirdelement
    print(thirdelement,end=" ")

