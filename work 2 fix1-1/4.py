char = input("Enter Character : ")
CharL = 0
CharU = 0
for C in char :

    if C.islower() == True:
        CharL = CharL+1
    if C.isupper() == True:
        CharU = CharU+1

if char.islower() == True:
    print("All Character is lower")
    print("Lower Character = ",CharL)
elif char.isupper() == True:
    print("ALL Character is Upper")
    print("Upper Character = ",CharU)


elif char.isupper() == False and char.islower() == False:
    print("Character Different")
    print("Lower Character = ",CharL)
    print("Upper Character = ",CharU)
