a=['thor','hulk','iron man','caption america']

#to create a copy of a list
b=[]
print(b)
b=a.copy()
print(b)

#to access an element
print(a.index("iron man"))

#to extend the list
c=['vision','spiderman']
a.extend(c)
print(a)

#to reverse the list
a.reverse()
print(a)

#to sort the list
a.sort()
print(a)

#to clear all the data from the list
a.clear()
print(a)