speed = float(input("speed = "))
if speed < 45:
    print("slow speed")
elif 45 <= speed < 90:
    print("moderate speed")
elif speed > 90:
    print("fast speed")