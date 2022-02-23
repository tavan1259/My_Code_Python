NStart = input("Enter Start Number = ")
NEnd = input("Enter End Number = ")

NStart = int(NStart)
NEnd = int(NEnd)
if NStart<0 or NEnd<0:
    print("Tye Again Chain Number")
else:
    Cal = [NStart]
    n1,n2 = NStart,NStart+1
    for R in range(NStart,NEnd):
        if n2<NEnd+1:
            Cal.append(n2)
            n1,n2 = n2,n1+n2

    print(Cal)