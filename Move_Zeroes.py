n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if i!=0:
        print(i,end=" ")
for i in lst:
    if i==0:
        print(i,end=" ")