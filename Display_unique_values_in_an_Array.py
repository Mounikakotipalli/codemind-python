num=int(input())
lst=list(map(int,input().split()))
new_lst=[]
for i in lst:
    if lst.count(i)==1:
        new_lst.append(i)
if len(new_lst)==0:
    print("-1")
else:
    for i in new_lst:
        print(i,end=" ")