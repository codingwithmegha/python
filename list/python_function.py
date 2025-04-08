a=['thor','hulk','iron man','caption america']

# to find the length of the list
print(len(a))

#to find the count of the list
print(a.count('thor'))

#to append the new item in the list
a.append('123')
print(a)

#to append the element in the specific location
a.insert(2,'spider man')
print(a)

#to remove the element from the list
a.remove('thor')
print(a)

#to remove the element using index
a.pop(2)
print(a)
