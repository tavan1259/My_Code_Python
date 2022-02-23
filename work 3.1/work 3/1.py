Num = int(input("Enter interest : "))
income =[10000,15000,20000,25000,30000,35000,40000]

Cal =[]
y = 0
if Num >= 0:
    while y < 4:
        y = y+1
        if y ==1 :
            for S in income:
                Cal.append("%.2f"%(S))
        for M in income:
            allM = M*((1+(Num/100))**y)
            Cal.append("%.2f"%(allM))
                    
    
    print(f"\nค่าดอกเบี้ย = {Num}\n")
    print(" year       1        2        3        4")
    for i in range(7):  
        print(f"{Cal[i]}|{Cal[i+7]}|{Cal[i+14]}|{Cal[i+21]}|{Cal[i+28]}|")
else:
    print("Error")
