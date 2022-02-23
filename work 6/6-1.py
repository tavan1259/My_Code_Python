class Car :
    def __init__(self, license, brand, color):
        self.license = license
        self.brand = brand
        self.color = color
        self.report = []

    def __str__(self):
        text = (f"{self.license} - {self.color} {self.brand}")
        return text
    
    def __lt__(self, rhs):
        return self.license < rhs.license


    def add_report(self, new_report):
        self.report.append(new_report)
        return self.report
    

    def total_payment(self):
        Cal_Num = 0
        for Num in self.report :
            Cal_Num += Num[2]
        return Cal_Num

    def max_payment(self):
        if len(self.report) <= 0 :
            return self.report
        else:
            print(f"ประวัติการซ่อมบำรุ่งที่ใช้ค่าใช้จ่ายมากที่สุด {max(self.report)[0]} {max(self.report)[1]}  {max(self.report)[2]} ")
            


F_c = Car('AA1234','Honda','White')
S_c = Car('AB1234','Toyota','Red')

print(f"คืนสตริงของรถยนต์ {F_c}")

print(f"เรียงลำดับรถยนต์ {S_c.__lt__(F_c)}")
print(f"เรียงลำดับรถยนต์ {S_c < F_c}")

F_c.add_report(('25 May 2017','change tires', 1500))
F_c.add_report(('5 Oct 2007','change window', 3000))

print(f"ค่าใช้จ่ายทั้งหมด = {F_c.total_payment()}")
F_c.max_payment()
print(f"กรณีที่รถยนต์ไม่มีประวัติ {S_c.max_payment()}")

#print(F_c.report)