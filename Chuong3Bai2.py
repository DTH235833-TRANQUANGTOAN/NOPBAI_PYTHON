thang=int(input("tháng mấy: "))
if thang in [1,3,5,7,8,10,12]:
    print("tháng",thang,"có 31 ngày")
elif thang in [4,6,9,11]:
    print("tháng",thang,"có 30 ngày")
elif thang==2:
    nam=int(input("nhập năm: "))
    if nam%400==0 or (nam%4==0 and nam%100!=0):
        print("tháng 2 có 29 ngày")
    else:
        print("tháng 2 có 28 ngày" )
else:
    print(thang,"nhập sai rồi!")