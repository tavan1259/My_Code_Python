y = int(input("Enter year = "))
if 0< y :
    if (y % 400 == 0) and (y % 4 == 0 ) or (y % 100 != 0) :
        print ("ture")
    else:
        print ("false")
else:
    print("tye again")