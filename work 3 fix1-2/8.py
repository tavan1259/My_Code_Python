Box = input("ใส่เลข 1 หลัก จำนวนไม่เกิน 10 และโปรดเว้นด้วยช่องว่างด้วย :").split()
P = ""
Raw = 0
Raw1 = 0
R1 = 0
T = 0
Show = []
CN = []
D = []
S = 0

if len(Box) >10:
    Raw = 3
while Raw == 0:
    
    for R in Box:
        C = R
        CN.clear()
        for Cnum in C:
            CN.append(Cnum)
        if len(CN) > 1:
            Raw = 4
        R = int(R)
        while R1 < len(Box):
            if R <= int(Box[R1]):
                T = T+1
                if T == len(Box):
                    Show.append(str(R))
                    Box.remove(str(R))
                    D.append(int(R))
            R1 = R1+1
        T = 0
        R1 = 0
    
    if len(Box) == 0 :
        Raw = 1

while Raw == 1:
    if int(Show[0]) == 0:
        Show.remove(str(0))
        Show.append('2')
        while Raw1 == 0:
            if int(Show[S]) > 1:
                Show.insert(S,str(0))
                Raw1=1
            S = S+1
        Show.pop(len(Show)-1)
    if int(Show[0]) != 0:
        Raw =2
    S=0
    Raw1=0

    
if Raw == 2:
    print(P.join(Show))
if Raw == 3:
    print("ตัวเลขเกินจำนวน โปรดใส่ใหม่")
if Raw == 4:
    print("มีจำนวนบางจำนวน เกิน 1 หลัก")