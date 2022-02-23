NStart = input("Enter Start Number = ")
NEnd = input("Enter End Number = ")
Spa = ","
NStart = int(NStart)
NEnd = int(NEnd)
if NStart<0 or NEnd<0:
    print("Tye Again Chain Number")
    
elif NStart >= 0 and NEnd >= 0:
    
    Cal = []
    n1,n2 = 0,1
    for R in range(NStart,NEnd):
        if n2<NEnd+1:
            n1,n2 = n2,n1+n2
            if n2>=NStart and n2<NEnd+1:
                if n1 == 1 and n2 == 1:
                    
                    Cal.append("0")
                    Cal.append("1")
                
                Cal.append(str(n2))
    
    
    print("Fibonacci = ",Spa.join(Cal))