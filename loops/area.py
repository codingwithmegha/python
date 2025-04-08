
print("***** AREA CALCULATOR*****")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")

choice=int(input("enter the choice between 1 -4: "))

if choice==1:
 side=float(input("enter the side: "))
 sq=side*side
 print("area of square: ",sq)

elif choice==2:
 length=float(input("enter the length: "))
 breadth=float(input("enter the breath: "))
 rectangle=length*breadth
 print("area of rectangle: ",rectangle)

elif choice==3:
    radius=float(input("enter the radius: "))
    circle=3.14*radius**2
    print("area of circle :",circle)

elif choice==4:
 base=float(input("enter the base: "))
 height=float(input("enter the height: "))
 triangle=1/2*base*height;
 print("area of triangle: ",triangle)

else:
    print("invalid number")