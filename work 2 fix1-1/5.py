add = []
Chack = []
Spa = ","
for num in range(1000,3000):
    num = str(num)
    if int(num[0])%2==0 and int(num[1])%2==0 and int(num[2])%2==0 and int(num[3])%2==0:
        num = str(num)
        add.append(num)
print(Spa.join(add))