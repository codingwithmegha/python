"""Continue statement :
continue statement is used when you want to skip a particular condition.
Break Statement :
Break Statement is used when you want to destroy a loop at a certain condition and come out of the loop."""


for i in range(1,8):
    if i==5:
        print("skip this song")
        continue
    else:
        print(i)


for i in range(1,5):
    if i==2:
        print("break this statement")
        break
    print(i)