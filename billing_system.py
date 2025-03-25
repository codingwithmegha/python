# WAP to create a billing system at supermarket.

while True:
    name=input("Customer_Name")
    total=0

    while True:
        print("Enter amount and qunatity")
        amount=float(input("enter amount: "))
        quantity=float(input("enter qunatity: "))
        total+=amount*quantity

        repeat=input("do want to add more iteams?(yes/no): ")
        if repeat=="no" or repeat=="No":
           break

    print("-"*40)
    print("Name: ",name)
    print("Amount to be paid: ",total)
    print("-"*40)
    print("**********Happy Shopping**************")
    repeat1=input("do you want to go to the next customer? (yes/no): ")
    if repeat1=="no" or repeat1=="No":
        break
