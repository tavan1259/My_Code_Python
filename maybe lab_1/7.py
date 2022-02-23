x = int(input("Select 1. (Rectangle) or 2. (Triangle) : "))
if x==1:
    wid,leng = input("Enter width,length = ").split(",")
    wid = float(wid)
    leng = float(leng)
    print("พื้นที่ของสี่เหลียม = ",wid*leng)

elif x == 2:
    bas,hei = input("Enter base,height = ").split(",")
    bas = float(bas)
    hei = float(hei)
    print("พื้นที่ของสามเหลือม = ",0.5*bas*hei)
else:
    print("please tye again")
