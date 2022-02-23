import random 
No = ['',' ',' ',' ',' ',' ',' ','']
Na = ['',' ',' ',' ',' ',' ',' ','']
Nb = ['',' ',' ',' ',' ',' ',' ','']
Nc = ['',' ',' ',' ',' ',' ',' ','']
Nd = ['',' ',' ',' ',' ',' ',' ','']
Ne = ['',' ',' ',' ',' ',' ',' ','']
Nf = ['',' ',' ',' ',' ',' ',' ','']
W = '|'
Tum = [Nf,Ne,Nd,Nc,Nb,Na,No]

Game = True

def TU(x):
    globals = Tum
    globals = Score
    for y in range(6):
        if Tum[y][x] != "x" and Tum[y][x] != "w":
            Tum[y].pop(x)
            Tum[y].insert(x,"x")
            
            if Tum [y][x-1] == "x" and Tum [y][x-2] == "x" or Tum [y][x+1] == "x" and Tum [y][x+2] == "x" or Tum [y][x-1] == "x" and Tum [y] [x+1] == "x"\
                    or Tum [y-1][x] == "x" and Tum [y-2][x] == "x" \
                    or Tum[y-1][x+1] == "x" and Tum[y+1][x-1] == "x" or Tum [y+1][x+1] == "x" and Tum[y-1][x-1] == "x" \
                    or Tum[y-1][x-1] == "x" and Tum[y-2][x-2] == "x" or Tum [y-1][x+1] == "x" and Tum[y-2][x+2] == "x" \
                    or Tum[y+1][x+1] == "x" and Tum[y+2][x+2] == "x" or Tum [y+1][x-1] == "x" and Tum[y+2][x-2] == "x":
                return 1
            break

def TC(x):
    globals = Tum
    globals = Score
    for y in range(6):
        if Tum[y][x] != "x" and Tum[y][x] != "w":
            Tum[y].pop(x)
            Tum[y].insert(x,"w")
            
            if Tum [y][x-1] == "w" and Tum [y][x-2] == "w" or Tum [y][x+1] == "w" and Tum [y][x+2] == "w" or Tum [y][x-1] == "w" and Tum [y] [x+1] == "w"\
                    or Tum [y-1][x] == "w" and Tum [y-2][x] == "w" \
                    or Tum[y-1][x+1] == "w" and Tum[y+1][x-1] == "w" or Tum [y+1][x+1] == "w" and Tum[y-1][x-1] == "w" \
                    or Tum[y-1][x-1] == "w" and Tum[y-2][x-2] == "w" or Tum [y-1][x+1] == "w" and Tum[y-2][x+2] == "w" \
                    or Tum[y+1][x+1] == "w" and Tum[y+2][x+2] == "w" or Tum [y+1][x-1] == "w" and Tum[y+2][x-2] == "w":
                return 2
            break

def Show():
    print(W.join(Na))
    print(W.join(Nb))
    print(W.join(Nc))
    print(W.join(Nd))
    print(W.join(Ne))
    print(W.join(Nf))

while Game:
    Show()
    Score = 0
    User = int(input("Enter Number (1-6) : "))
    if User > 6 or User < 0:
        print("ท่านใส่ค่าเกินกำหนดโปรดเริ่มใหม่")
        break
    
    if TU(User) == 1:
        Show()
        print("you win !!!")
        break

    computer = random.randint(1,6)
    print("computer Chost : ",computer)
    
    if TC(computer) == 2:
        Show()
        print("Bot win !!!")
        break


    



