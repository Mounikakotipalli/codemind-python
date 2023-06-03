num=int(input())
nurev=str(num)[::-1]
sqrev=str(int(nurev)**2)[::-1]
print(num**2==int(sqrev))