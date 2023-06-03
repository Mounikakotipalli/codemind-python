num=input()
su=0
for i in range(0,len(num)):
    su+=int(num[i])**(i+1)
print(int(num)==su)