if max(D)<2:
        S2 = 0
        Raw = 2
while S2 == 0:
    if int(Show[0]) == 0:
        Show.remove(str(0))
        Show.append(str(0))
    if int(Show[0]) != 0:
        S2 = 1