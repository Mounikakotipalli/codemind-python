num=input()
lst=list(num)
se=set(num)
if len(se)==len(lst):
    print("Unique Number")
else:
    print("Not Unique Number")