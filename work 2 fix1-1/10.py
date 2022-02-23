Roman = input("Enter Roman Number = ")
Cal1 = []
Num = 0
befor = ""
for R1 in Roman:
    
    for R11 in R1:
        

        if (R11 == "M" or R11 == "m") and (befor == "d"):
            Num = Num+0
            Cal1.append(Num)
            Num = 0
            befor = "m"
            break
        elif (R11 == "M" or R11 == "m") and (befor == "c"):
            Num = Num+800
            Cal1.append(Num)
            Num = 0
            befor = "m"
            break
        elif (R11 == "M" or R11 == "m") and (befor == "l"):
            Num = Num+900
            Cal1.append(Num)
            Num = 0
            befor = "m"
            break
        elif (R11 == "M" or R11 == "m") and (befor == "x"):
            Num = Num+980
            Cal1.append(Num)
            Num = 0
            befor = "m"
            break
        elif (R11 == "M" or R11 == "m") and (befor == "v"):
            Num = Num+990
            Cal1.append(Num)
            Num = 0
            befor = "m"
            break
        elif (R11 == "M" or R11 == "m") and (befor == "i"):
            Num = Num+998
            Cal1.append(Num)
            Num = 0
            befor = "m"
            break
        elif R11 == "M" or R11 == "m":
            Num = Num+1000
            befor = "m"
        

        if(R11 == "D" or R11 == "d") and (befor == "c"):
            Num= Num+100
            Cal1.append(Num)
            Num = 0
            befor = "d"
            break
        elif(R11 == "D" or R11 == "d") and (befor == "l"):
            Num = Num+400
            Cal1.append(Num)
            Num = 0
            befor = "d"
            break
        elif(R11 == "D" or R11 == "d") and (befor == "x"):
            Num = Num+480
            Cal1.append(Num)
            Num = 0
            befor = "d"
            break
        elif(R11 == "D" or R11 == "d") and (befor == "v"):
            Num = Num+490
            Cal1.append(Num)
            Num = 0
            befor = "d"
            break
        elif(R11 == "D" or R11 == "d") and (befor == "i"):
            Num = Num+498
            Cal1.append(Num)
            Num = 0
            befor = "d"
            break
        elif R11 == "D" or R11 == "d":
            Num = Num+500
            befor = "d"


        if(R11 == "C" or R11 == "c") and (befor == "l"):
            Num = Num+0
            Cal1.append(Num)
            Num = 0
            befor = "c"
            break
        elif(R11 == "C" or R11 == "c") and (befor == "x"):
            Num = Num+80
            Cal1.append(Num)
            Num = 0
            befor = "c"
            break
        elif(R11 == "C" or R11 == "c") and (befor == "v"):
            Num = Num+95
            Cal1.append(Num)
            Num = 0
            befor = "c"
            break
        elif(R11 == "C" or R11 == "c") and (befor == "i"):
            Num = Num+98
            Cal1.append(Num)
            Num = 0
            befor = "c"
            break
        elif R11 == "C" or R11 == "c":
            Num = Num+100
            befor = "c"
        

        if(R11 == "L" or R11 == "1")and(befor == "X"):
            Num = Num+30
            Cal1.append(Num)
            Num = 0
            befor = "l"
            break
        elif(R11 == "L" or R11 == "l")and(befor == "v"):
            Num = Num+40
            Cal1.append(Num)
            Num = 0
            befor = "l"
            break
        elif(R11 == "L" or R11 == "l")and (befor == "i"):
            Num = Num+48
            Cal1.append(Num)
            Num = 0
            befor = "l"
            break
        elif R11 == "L" or R11 == "l":
            Num = Num+50
            befor = "l"


        elif (R11 == "X" or R11 == "x") and (befor == "v"):
            Num = Num+0
            Cal1.append(Num)
            Num = 0
            befor = "x"
            break
        elif (R11 == "X" or R11 == "x") and (befor == "i"):
            Num = Num+8
            Cal1.append(Num)
            Num = 0
            befor = "x"
            break   
        elif R11 == "X" or R11 == "x":
            Num = Num+10
            befor = "x"


        if (R11 == "V" or R11 == "v") and (befor == "i"):
            Num = Num+3
            Cal1.append(Num)
            Num = 0
            befor = "v"
            break
        elif R11 == "V" or R11 == "v":
            Num = Num+5
            befor = "v"


        if R11 == "I" or R11 == "i":
            Num = Num+1
            befor = "i"
Cal1.append(Num)


print("Roman Number : %s = Number : %d "%(Roman,sum(Cal1)))
for R2 in Roman:
    if R2 not in ["i","v","x","l","c","d","m","I","V","X","L","C","D","M"]:
        print("%s --->This is not Roman Number !!!"%(R2))
