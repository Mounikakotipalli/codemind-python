a=int(input())
b=int(input())
for i in range(a,b+1):
    rev=str(i)[::-1]
    if(int(rev)==i):
        print(i,end=" ")