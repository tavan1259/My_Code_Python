Num = int(input("Enter Number : "))
NumUnder = Num-1
def Cal (NM):
    NumUnder = Num-1

    Show = ""
    Be = 0
    for Char in range(Num+1):
        Chark = Num-Char
        if Char > Be:
            for b in range(Be+1):
                Show += str(b)
        Show += str(Char)
        
        for R1 in range(Chark):
            Show += str(Char)
            Show += str(Char)
        
        if Char > Be:
            while Be != 0 :
                Show += str(Be)
                Be -= 1
            Show += str(0)
        Be = Char
        Show += "\n"
    Be = Num
    
    while NumUnder != -1:
        hark = Num - NumUnder
        if NumUnder < Be:
            for b in range(NumUnder):
                Show += str(b)
        for R1 in range(hark):
            Show += str(NumUnder)
            Show += str(NumUnder)
        Be = NumUnder
        if NumUnder <= Be:
            while Be != 0 :
                Show += str(Be)
                Be -= 1
            Show += str(0)
        Be = NumUnder
        Show += "\n"
        NumUnder -= 1
    print(Show)
if Num > 9 or Num < 0:
        print("โปรดระบุ ค่าใหม่")
else:
    Cal(Num)