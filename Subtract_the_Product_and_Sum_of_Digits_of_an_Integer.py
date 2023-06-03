num=input()
pro=1
su=0
for i in num:
    pro*=int(i)
    su+=int(i)
print(pro-su)