num = int(input("Enter Number : "))
test =[]
for inum in range (0,num+1,5):
    cal = str(inum)
    test.append(cal)

    P="+"
    print(P.join(test))
    
