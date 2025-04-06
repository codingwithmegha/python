"""
List are the collection of ordered and mutable data.
* lists are written inside the square brackets.\
* the value inside the list is seperated by ,.
* multiple data type can be written inside the list.
"""

fruits=['apple','banana','orange',1,32,43.2]
print(fruits)
print(type(fruits))


#slicing list
a=['iron man','thor','caption america','hulk']

#to access any element from the list
print(a[1],a[-1])
print(a[2:4])
print(a[:2])
print(a[::2])

#to get the reverse of the list
print(a[::-1])