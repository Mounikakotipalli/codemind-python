num=input()
sqr=int(num)**2
new=str(sqr)[len(str(sqr))-len(num):len(str(sqr))]
if new==num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")