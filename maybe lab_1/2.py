x = int(input("you score = "))
if 0 <= x < 50:
    print("Grade = F")
elif 50 <= x < 80:
    print("Grade = P")
elif 80 <= x <= 100:
    print("Grade = G")
else:
    print("plese tye again")