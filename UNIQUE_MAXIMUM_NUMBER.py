a=int(input())
n=list(map(int, input().split()))
new_lst=[]
for i in n:
    if n.count(i)==1:
        new_lst.append(i)
if len(new_lst)==0:
    print("-1")
else:
    print(max(new_lst))