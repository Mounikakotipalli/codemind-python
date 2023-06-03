n=int(input())
lst=list(map(int,input().split()))
a=int(input())
lst1=list(map(int,input().split()))
tar=int(input())
count=0
for i in range(0,n):
    if tar in range(lst[i],lst1[i]+1):
        count+=1
print(count)