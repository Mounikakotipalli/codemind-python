def is_prime(val):
    for i in range(2,int(val**0.5)+1):
        if val%i==0:
             return False
    return True
a=int(input())
n=list(map(int, input().split()))
ppro=1
nppro=1
for i in n:
    if(is_prime(i)):
        ppro*=i
    else:
        nppro*=i
print(abs(ppro-nppro))