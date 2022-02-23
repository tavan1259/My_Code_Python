
rule = 0
rule2 = 0

Num1 = 1
Num2 = 1
Cal = 0

Chr = []
Pal = []

markf = 0
markl = 0
Mcal1 = 0
Mcal2 = 0
Callen = 0
while rule == 0:
    Cal = Num1*Num2

    for R in str(Cal):
        Chr.append(int(R))
    markl = len(Chr)-1

    if len(Chr) >2:
        while rule2 == 0:
            
            if markf == markl:
                Pal.append(Cal)
                rule2 = 1
                Callen = 0
                
            if markf-markl >0:
                Pal.append(Cal)
                rule2 = 1
                Callen = 0
            
            Callen = Chr[markf] - Chr[markl]
            if Callen != 0:
                rule2 = 1
                Callen = 0
               
            markf = markf+1
            markl = markl-1
            Callen = 0
        markf = 0
            
            
    if Num1 > 999:
        Num1 = 0
        Num2 =Num2+1
        
    Num1 =Num1+1
    if Num2 == 999:
        rule =1
    Chr.clear()
    rule2 = 0
print(max(Pal))
