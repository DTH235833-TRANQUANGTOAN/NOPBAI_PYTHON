import math

try:
    r=float(input("Nhap ban kinh hinh tron: "))
    cv=2*math.pi*r
    dt=r**2
    print("chui vi: ",cv)
    print("dien tich: ",dt)
except:
    print("loi")
