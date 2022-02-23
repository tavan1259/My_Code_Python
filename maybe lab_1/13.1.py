Pizza = int(input("Pizza 5 ดาว \n ถาดเล็ก 99 บาท เลือกหมายเลข 1 \n ถาดกลาง 199 บาท เลือกหมายเลย 2 \n ถาดใหญ่ 299 บาท เลือกหมายเลข 3 \n\n คุณเลือกขนาด Pizza หมายเลข = "))

allMoney = 0
if Pizza == 1 :
    PS =99
    sizeS = 20
    sp = 20
    
    Siz = input("\n\nเพิ่มขอบชีช โปรดเลือก(y/n) =")
    if Siz == "y":
        PS = PS+sizeS 
        print("ท่านเพิ่มขอบชีช")
    elif Siz == "n":
        print("ท่านไม่ต้องการเพิ่มขอบชีช")
    else:
        print("ท่านใส่ผิดตัวอักษร")

    Spi = input("\nเพิ่มหน้า โปรดเลือก(y/n) =")
    if Spi == "y":
        PS = PS+sp
        print("ท่านเพิ่มหน้า")
    elif Spi == "n":
        print("ท่านไม่ต้องการเพิ่มหน้า")
    else:
        print("ท่านใส่ผิดตัวอักษร")

    allMoney = PS


elif Pizza == 2:
    PM =199
    sizeM = 30
    sp = 20

    Siz = input("\nเพิ่มขอบชีช โปรดเลือก(y/n) =")
    if Siz == "y":
        PM = PM+sizeM
        print("ท่านเพิ่มขอบชีช")
    elif Siz == "n":
        print("ท่านไม่ต้องการเพิ่มขอบชีช")
    else:
        print("ท่านใส่ผิดตัวอักษร")

    Spi = input("\nเพิ่มหน้า โปรดเลือก(y/n) =")
    if Spi == "y":
        PM = PM+sp
        print("ท่านเพิ่มหน้า")
    elif Spi == "n":
        print("ท่านไม่ต้องการเพิ่มหน้า")
    else:
        print("ท่านใส่ผิดตัวอักษร")

    allMoney = PM


elif Pizza == 3:
    sizeB = 40
    PB =299
    sp = 20

    Siz = input("\nเพิ่มขอบชีช โปรดเลือก(y/n) =")
    if Siz == "y":
        print("ท่านเพิ่มขอบชีช")
        PB = PB+sizeB
    elif Siz == "n":
        print("ท่านไม่ต้องการเพิ่มขอบชีช")
    else:
        print("ท่านใส่ผิดตัวอักษร")

    Spi = input("\nเพิ่มหน้า โปรดเลือก(y/n) =")
    if Spi == "y":
        PB = PB+sp
        print("ท่านเพิ่มหน้า")
    elif Spi == "n":
        print("ท่านไม่ต้องการเพิ่มหน้า")
    else:
        print("ท่านใส่ผิดตัวอักษร")

    allMoney = PB

if allMoney:  
    print("\nรวมราคาทั้งหมด : ",allMoney)
    
if Pizza > 4:
    print("โปรดเริ่มรายการใหม่")