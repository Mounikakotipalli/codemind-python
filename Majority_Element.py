n=int(input())
lst=list(map(int,input().split()))
for i in lst:
  if lst.count(i)>n//2:
    print(i)
    break