num=int(input())
su=0
while 1:
    su=0
    if num<10:
        print(num==1 or num==7)
        break
    for i in str(num):
        su+=int(i)**2
        num=su