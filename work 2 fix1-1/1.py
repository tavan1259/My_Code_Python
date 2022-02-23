num = input("Enter Number : ")
testint = 0
test =[]
CalNum =[]
num = int(num)
if num >= 0:
    
    for inum in range (0,num,5):
        cal = str(inum)
        test.append(cal)
        CalNum.append(inum)
        P="+"
    #CalNum.append(num)
    #test.append(str(num))
    print("ค่าที่รับมา %d นำไปคำนวน %s จะได้ %d "%(num,P.join(test),sum(CalNum)))
else:
    print("Error")


