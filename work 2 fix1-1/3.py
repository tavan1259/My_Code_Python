num = int(input("Enter Number :"))
lsnum = []
if num > 0 :
    for inum in range(0,num):
        if (inum%2==0 and inum%3==0) or (inum%2!=0 and inum%3!=0):
            lsnum.append(inum)
    print("เลขที่ออก = ",lsnum)
else:
    print("Error")
