num=input()
su=0
while int(num)>9:
    su=0
    for i in num:
        su+=int(i)
        num=str(su)
print(num)