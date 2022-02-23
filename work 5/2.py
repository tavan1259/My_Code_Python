Num = int(input("Enter Number : "))
Whi = " "
def Cal():
    
    NumUn = Num-1
    BF = 0
    Show =""
    for Rup in range(Num+1):
        Show += str(Whi*(Num-Rup))
        if Rup > BF:
            for b in range(BF+1):
                Show += str(b)
        Show += str(Rup)

        if Rup > BF :
            while BF!=-1:
                Show +=str(BF)
                BF -= 1
        BF = Rup
        Show += "\n"
    BF = Num

    while NumUn != -1:
        if NumUn < BF:
            Show += Whi*(Num-NumUn)
            for b in range(NumUn+1):
                Show += str(b)
            BF = NumUn-1
            while BF !=-1:
                Show += str(BF)
                BF -= 1
            BF = NumUn
        Show += "\n"
        NumUn -= 1
    print(Show)
if Num > 9 or Num < 0:
        print("โปรดระบุ ค่าใหม่")
else:
    Cal()
