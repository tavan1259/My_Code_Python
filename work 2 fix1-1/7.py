Num1,Num2 = input("Enter 2 Number : ").split()
Num = [Num1,Num2]
Min = int(min(Num))
Max = int(max(Num))
NStep1 = []
NStep2 = []
NStep3 = 0
if Min >0 or Max > 0:
    for R1 in range(1,Min+1):
        if Min%R1==0:
            NStep1.append(R1)
    for R2 in range(1,Max+1):
        if Max%R2==0:
            if R2 in NStep1:
                NStep3 = R2

    print("ค่า ห.ร.ม. ที่ได้ คือ ",NStep3)
else:
    print("Tye Again")