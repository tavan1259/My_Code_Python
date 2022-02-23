Kmitl = ['*****',
         '*MM**',
         '*KIK*',
         '*IT**',
         '**L**',
        ]
Kqa = []
Mqa = []
Iqa = []
Tqa = []
Lqa = []
for y in range(5):
    xk = 0
    for x in Kmitl[y]:
        if x == "K":
            Kqa.append(str(y)+str(xk))
            print(str(y)+str(xk))
        
            for kk in Kqa:
                kky = int(kk[0])
                kkx = int(kk[1])
                for y1 in range(5):
                    xm = 0
                    for x1 in Kmitl[y1] :
                        if x1 == "M" and (xm == (kkx-1) or xm == (kkx+1) or xm == (kkx+0)) and (y1 == (kky-1) or y1 == (kky+1) or y1 == kky):

                            Mqa.append(str(y1)+str(xm))
                            print(str(y1)+str(xm))

                            for mm in Mqa:
                                mmy = int(mm[0])
                                mmx = int(mm[1])
                                for y2 in range(5):
                                    xi = 0
                                    for x2 in Kmitl[y2]:
                                        if x2 == "I" and ( xi == (mmx-1) or xi == (mmx+1) or xi == mmx) and ( y2 == (mmy-1) or y2 == (mmy+1) or y2 == mmy ):
                                            Iqa.append(str(y2)+str(xi))
                                            print(str(y2)+str(xi))

                                            for ii in Iqa:
                                                iiy = int(ii[0])
                                                iix = int(ii[1])
                                                for y3 in range(5):
                                                    xt = 0
                                                    for x3 in Kmitl[y3]:
                                                        if x3 == "T" and ( xt == (iix-1) or xt == (iix+1) or xt == iix ) and ( y3 == (iiy-1) or y3 == (iiy+1) or y3 == iiy ) :
                                                            Tqa.append(str(y3)+str(xt))
                                                            print(str(y3)+str(xt))
                                                            
                                                            for tt in Tqa:
                                                                tty = int(tt[0])
                                                                ttx = int(tt[1])
                                                                for y4 in range(5):
                                                                    xl = 0
                                                                    for x4 in Kmitl[y4]:
                                                                        if x4 == "L" and ( xl == (ttx-1) or xl == (ttx+1) or xl == ttx ) and ( y4 == (tty-1) or y4 == (tty+1) or y4 == tty )  :
                                                                            Lqa.append(str(y4)+str(xl))
                                                                            print(str(y4)+str(xl))

                                                                            print("K "+str(y+1)+" "+str(xk+1)+" M "+str(y1+1)+" "+str(xm+1)+" I "+str(y2+1)+" "+str(xi+1)+" T "+str(y3+1)+" "+str(xt+1)+" L "+str(y4+1)+" "+str(xl+1))
                                                                            
                                                                        xl += 1
                                                                print("*************")
                                                                Tqa.pop(0)
                                                        xt += 1
                                                print("++++++++++")
                                                Iqa.pop(0)
                                        xi += 1
                                print("------------")
                                Mqa.pop(0)
                        xm += 1
                print("==============")
                Kqa.pop(0)
        xk+=1

        
                    
                        

        
    
#print(CK)
#print(CM)
#print(" ".join(Kqa))
#print(" ".join(Mqa))