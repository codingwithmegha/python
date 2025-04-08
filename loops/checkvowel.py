# WAP to check whether the passes letter is vowel or not.
letter=input("enter the alphabet: ")
#if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
if letter in "aeiou" or letter in"AEIOU":
 print(letter,"is a vowel")
else:
 print(letter,"is not a vowel")