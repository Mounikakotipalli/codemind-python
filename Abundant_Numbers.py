num=int(input())
su=0
for i in range(1,num):
    if(num%i==0):
        su+=i
print(su>num)