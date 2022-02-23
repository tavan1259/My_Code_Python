M = int(input("Mid-term Full(100) = "))
F = int(input("Final Full(100) = "))
H = int(input("Homework Full(10) = "))
if ((M<0) or (F<0) or (H<0)) or ((M>100) or (F>100) or (H>10)):
    print("ขออภัยโปรดใส่คะแนนน้องใหม่ด้วย")
else:
    x = (M*40)/100 + (F*50)/100 + H
    if 0 <= x < 50:
        print("ได้เกรด  F")
    elif 50 <= x < 55 :
        print("ได้เกรด  D")
    elif 55 <= x < 60 : 
        print("ได้เกรด  D+")
    elif 60 <= x < 70 :
        print("ได้เกรด  C")
    elif 70 <= x < 80 :
        print("ได้เกรด  C+")
    elif 80 <= x < 85 :
        print("ได้เกรด  B")
    elif 85 <= x < 90 :
        print("ได้เกรด  B+")
    elif 90 <= x <= 100 :
        print("ได้เกรด A")
    else :
        print("โปรดใ่ส่คะแนนใหม่")