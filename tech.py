list=["muiz","tayyab","shahaid","noor"]
A=0
while A<len(list):
    if list[A]=="shahaid":
         A+=1
         continue
    print(list[A])
    A+=1

num=0
while num<=10:
     if num==5:
            num+=1
            continue
     print(num)
     num+=1 