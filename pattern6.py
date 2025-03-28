"""
1      i=1     1*i
21     i=2     2*i
321     i=3    3*i
4321
54321
"""

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()