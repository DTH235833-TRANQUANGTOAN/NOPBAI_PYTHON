from math import sqrt
print ("giải phương trình ax^2+by+c=0")
a=float(input("nhập a: "))
b=float(input("nhập b: "))
c=float(input("nhập c: "))
if a==0:
    if b==0:
        if c==0:
            print("phương trình có vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        print("phương trình có một nghiệm: x=", -c/b) 
else:
    denta=b**2-4*a*c
    if denta<0:
        print("phương trình vô nghiệm")
    elif denta==0:
        x=-b/(2*a)
        print("phương trình có nghiệm kép: x1=x2=",x)
    else:
        x1=(-b+sqrt(denta))/(2*a)
        x2=(-b-sqrt(denta))/(2*a)
        print("phương trình có hai nghiệm phân biệt:")
        print("x1=",x1)
        print("x2=",x2)
    
