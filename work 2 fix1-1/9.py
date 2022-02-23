Num = input("Enter 1 Number = ")
NStep1 = []
SStep1 = []
P="+"
Num = int(Num)
if Num>=0:
    Num = str(Num)
    for R1 in range(1,5):
        RStep1 = Num*R1
        NStep1.append(int(RStep1))
        SStep1.append(str(RStep1))



    print("Output : %d  (=%s)"%(sum(NStep1),P.join(SStep1)))
elif Num<0:
    print("Error")
