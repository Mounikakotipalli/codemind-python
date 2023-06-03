num=int(input())
for i in range(1,num+1):
    for j in range(i,num+1):
        print(chr(65+num-i),end=" ")
    print()