Pizza = int(input("Pizza 5 ดาว \n ถาดเล็ก 99 บาท เลือกหมายเลข 1 \n ถาดกลาง 199 บาท เลือกหมายเลย 2 \n ถาดใหญ่ 299 บาท เลือกหมายเลข 3 \n\n คุณเลือกขนาด Pizza หมายเลข = "))

allMoney = 0
if Pizza == 1 :
    PS =99
    sizeS = 20
    sp = 20
    
    Siz = input("\nเพิ่มขอบชีช กด y หากไม่ต้องการกด n =")
    if Siz == "y":
        PS = PS+sizeS 
    else:
        print("ท่านไม่ต้องการเพิ่มขอบชีช")

    Spi = input("\nเพิ่มหน้า กด y หากไม่ต้องการกด n =")
    if Spi == "y":
        PS = PS+sp
    else:
        print("ท่านไม่ต้องการเพิ่มหน้า")
    allMoney = PS


elif Pizza == 2:
    PM =199
    sizeM = 30
    sp = 20
    Siz = input("\nเพิ่มขอบชีช กด y =")
    if Siz == "y":
        PM = PM+sizeM
    else:
        print("ท่านไม่ต้องการเพิ่มขอบชีช")

    Spi = input("\nเพิ่มหน้า กด y =")
    if Spi == "y":
        PM = PM+sp
    else:
        print("ท่านไม่ต้องการเพิ่มหน้า")
    allMoney = PM


elif Pizza == 3:
    sizeB = 40
    PB =299
    sp = 20
    Siz = input("\nเพิ่มขอบชีช กด y =")
    if Siz == "y":
        PB = PB+sizeB
    else:
        print("ท่านไม่ต้องการเพิ่มขอบชีช")

    Spi = input("\nเพิ่มหน้า กด y =")
    if Spi == "y":
        PB = PB+sp
    else:
        print("ท่านไม่ต้องการเพิ่มหน้า")
    allMoney = PB

if allMoney:  
    print("\nรวมราคาทั้งหมด : ",allMoney)
if Pizza > 4:
    print("โปรดเริ่มรายการใหม่")