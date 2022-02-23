N = int(input("Enter Number = "))
M = N%10
L = str(N)
if N>0:
    Num = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

    print(L[-1:]+" = "+Num[M])
else:
    print("tyeagain")