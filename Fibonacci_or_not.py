def fib(val):
    a=0
    b=1
    while(1):
        if a>val:
            print("False")
            break
        elif a==val:
            print("True")
            break
        c=a+b
        a=b
        b=c
num=int(input())        
fib(num)