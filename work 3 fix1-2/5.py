Num = []
Num2 = []
Ren = 0
R=2
C=0
Show = 0
Round = 1000
while Ren <= Round:
    for i in Num :
        if R%i==0:
            C = 0
            break
        elif R % i != 0:
            C = C+1
            if C == len(Num):
                Ren = Ren+1
                C = 0
                Num2.append(R)
                if Ren  == Round:
                    Show = R
    Num.append(R)
    R=R+1
print("จำนวนเฉพาะตัวที่ %d คือ %d "%(len(Num2),Show))


