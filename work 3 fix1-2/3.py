Num = 1
Save = 0
Move = 0
while Move == 0 :
    for R in range(1,20):
        if Num % R ==0:
            Save = Save+1
        elif Num % R !=0:
            Save = 1
            break
    if Save == 10:
        Move = 1
    
    Num = Num+1
    
print(Num-1)