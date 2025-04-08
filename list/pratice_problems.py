a=['megha','shivek','disha','bhumi']
print(a)

#WAP to swap first and fourth element in the list.
a[0],a[1]=a[1],a[0]
print(a)

#WAP to add new value at second position.
a.insert(1,'dipanshu')
print(a)

#WAP to delete a value from fourth position.
a.pop(3)
print(a)

#WAP to multiply all the element in the given list.
b=[13,7,12,10]
for i in b:
    c=b[i]*b[i+1]
print(c)