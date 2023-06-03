a=int(input())
lst=list(map(int, input().split()))
sue=0
suo=0
for i in range(0,len(lst)):
    if i%2==0:
        sue+=lst[i]
    else:
        suo+=lst[i]
if sue-suo==0:
    print("YES")
else:
    print("NO")