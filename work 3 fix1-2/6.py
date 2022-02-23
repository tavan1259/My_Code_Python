SumTSq = 1
SqTSum = 1
Cal = 0 
Cal2 = 0
while SumTSq<101:
    Pcal = SumTSq**2
    Cal = Cal+Pcal
    Pcal = 0
    SumTSq = SumTSq+1

while SqTSum<101:
    Cal2 = Cal2+SqTSum
    SqTSum =SqTSum+1
Cal2 = Cal2**2
print("ผลต่างระหว่าง square of the sum กับ sum of the squares = %d - %d = %d"%(Cal2,Cal,Cal2-Cal))
