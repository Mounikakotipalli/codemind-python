a=int(input())
b=int(input())
su_a=0
su_b=0
for i in range(1,a//2+1):
    if(a%i==0):
        su_a+=i
for i in range(1,b//2+1):
    if(b%i==0):
        su_b+=i
if su_a==b and su_b==a:
    print("Amicable")
else:
    print("Not Amicable")