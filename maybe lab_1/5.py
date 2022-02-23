a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if (a>b) and (a<c) or (a>c) and (a<b):
    print("a = ",a)

elif (b>a) and (b<c) or (b>c) and (b<a):
    print("b = ",b)

elif (c>a) and (c<b) or (c>b) and (c<a):
    print("c = ",c)


if (a==b) and (a==c):
    print("Mid is by a b and c =",a)
    
elif (a==b):
    print("Mid is by a and b = ",b)

elif (a==c):
    print("Mid by a and c = ",c)

elif (b==c):
    print("Mid is by b and c = ",c)
