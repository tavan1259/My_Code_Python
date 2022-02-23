Num = 1
Pri = 600851475143
SNum = []
Cal = 1
P = ","
for R in range(2,10000):
    if R % R ==0 and R % 1 ==0 and R % 2 != 0 and R % 3 != 0 :
        if Pri % R == 0:
            Pri = Pri/R
            SNum.append(str(R))
            for R2 in SNum:
                Cal = Cal*int(R2)
print(P.join(SNum))