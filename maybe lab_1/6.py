x = int(input("How old are you = "))
if 0 <= x < 11:
    print("Children")
elif 11 <= x < 21:
    print("Teenage")
elif 21 <= x < 36:
    print("Adult")
elif 36 <= x < 56:
    print("Middle age")
elif  x >= 56:
    print("Old age")
else :
    print("โปรดระบุใหม่")