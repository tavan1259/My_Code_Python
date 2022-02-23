print("Time In ")
HourIn = int(input("Enter Hour : "))
MinIn = int(input("Enter Minute : "))
print("Time out")
HourOut = int(input("Enter Hour : "))
MinOut = int(input("Enter Minute : "))

Money = 0

M = 0
H = 0
if HourIn >=7 and HourIn <=23 and HourOut >=7 and HourOut <=23:
    Time =1

if HourIn <7 or HourIn >23 or HourOut <7 or HourOut >23:
    Time =0


if HourIn < HourOut:
    H = HourOut-HourIn
elif HourOut < HourIn:
    H = HourOut(+24)-HourIn

if MinIn < MinOut :
    M = MinOut-MinIn
elif MinOut < MinIn:
    M = (MinOut+60)-MinIn
    H = H-1

if M <=15 and H ==0:
    print(" Free Time ")
elif (H<=2)or(M==0 and H ==3):
    Money = Money+10
elif (H<=5 and M>0) or (M==0 and H==6):
    Money = Money+50
elif H>= 6 and M >= 0:
    Money = Money+200

if Time ==1 :
    print("You need pay = %d"%(Money))
    
if Time ==0 :
    print("ขออภัยเวลาที่ลงนี้ยังไม่ได้เปิดให้บริการโปรดระบุใหม่")
    
