a="hello"
b="hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123@"
g="1.234"

#isalnum-return true if all characters in string are alphanumeric
print("*********alphanumeric*************")
print(a,a.isalnum())
print(b,b.isalnum())
print(f,f.isalnum())

#isalpha-return true if all character in the string are in alphabet
print("***********alphabet*************")
print(a,a.isalpha())
print(b,b.isalpha())

#isdecimal-return true if all character in the string are decimal
print("*************isdecimal****************")
print(a,a.isdecimal())
print(g,g.isdecimal())
print(c,c.isdecimal())

#isdigit- return true if all characters in the string are digit
print("*************string r digit****************")
print(c,c.isdigit())
print(g,g.isdigit())

#isnumeric- returns true if all characters in the string are numeric
print("**************string are numeric*************")
print(c,c.isnumeric())
print(g,g.isnumeric())
print(b,b.isnumeric())

#islower- convert string into lowercase
print("********lower************")
print(d,d.islower())
print(b,b.islower())
print(a,a.islower())

#isupper-convert string into upper case
print("*********upper*************")
print(d,d.isupper())


#isspace- returns true if all characters in the string are whitespace
print("***********whitespace****************")
print(e,e.isspace())
print(f,f.isspace())

#istitle- returns true if the string follows the rules of a title.
print("**********title********")
print(f,f.istitle())
print(a,a.istitle())
print(d,d.istitle())