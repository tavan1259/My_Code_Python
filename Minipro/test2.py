def A_TO_11(a,b) :
    if b.count(11) >= 1:
        while sum(b) > 16 and b.count(11) >= 2:
            b.insert(b[-1],1)
            b.pop(b.index(11))
        if len(b) > 2 and sum(b) > 21:
            b.insert(b[-1],1)
            b.pop(b.index(11))
    if a.count(11) >= 1:
        while sum(a) > 16 and a.count(11) >= 2:
            a.insert(a[-1],1)
            a.pop(a.index(11))
        if len(a) == 2 and sum(a) > 21:
            a.insert(a[-1],1)
            a.pop(a.index(11))
m = [3, 3, 8, 3, 11]
n = [11,9,7]
A_TO_11(n,m)
print(m)
print(n)

