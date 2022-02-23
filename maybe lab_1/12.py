n1,n2,n3,n4 = input("Please Enter 4 number (ex.1 2 3 4) =").split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
stataus = True
sum = n1+n2+n3+n4
if sum >1:
        if ((n1>=n2) and (n1>=n3) and (n1>=n4)) or ((n1<=n2) and (n1<=n3) and (n1<=n4)):
            r1 = n1
            sum = sum-n1
            if r1==n2 or r1==n3 or r1==n4 :
                stataus = False
        if ((n2>=n1) and (n2>=n3) and (n3>=n4)) or ((n2<=n1) and (n2<=n3) and (n2<=n4)):
            r2 = n2
            sum = sum-n2
            if r2==n1 or r2==n3 or r2==n4 :
                stataus = False
        if ((n3>=n1) and (n3>=n2) and (n3>=n4)) or ((n3<=n1) and (n3<=n2) and (n3<=n4)):
            r3 = n3
            sum = sum-n3
            if r3==n2 or r3==n1 or r3==n4 :
                stataus = False
        if ((n4>=n1) and (n4>=n2) and (n4>=n3)) or ((n4<=n1) and (n4<=n2) and (n4<=n3)):
            r4 = n4
            sum = sum-n4
            if r4==n2 or r4==n3 or r4==n1 :
                stataus = False

        
else:
    print("please tye again")
if not stataus:
    print("error")
else:
    print(sum)


