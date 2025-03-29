#endswith()-return true if the string ends with the specified value
a="megha tomar"
print(a.endswith("g",1,3))
print(a,a.endswith("r"))

#startwith()- Return true if the string starts with the specific value
b="shivek dhama"
print(b,b.startswith("s"))
print(b.startswith("d",7,10))

#swapcase()- Swap cases, lower case become upper case and vice versa
c="MEGHA"
d="shivek"
print(c,c.swapcase())
print(d,d.swapcase())

#strip()-return a trimmed version of the string
f="    **********megha tomar............."
print(f)
print(f.strip())

#split()-Splits the string at the specified separators, and returns a list
a="me#gh#as#hivek# megha#shivek#"
print(a.split("#"))

#ljust()-return a left justified version of the string
a="harry potter"
x=a.ljust(20)
print(x,"is my favt movie")