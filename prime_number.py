num=int(input())
s=0
for i in range(2,int(num**0.5)+1):
    if(num%i==0):
        print("not a prime")
        s=1
        break
if s!=1:
    print("prime")