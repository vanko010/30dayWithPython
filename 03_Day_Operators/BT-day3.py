import math
#Câu 1
age = 100.1010
age = int(age)
print(age)

#Câu 2
height = 1.59
h=float(height)
print(h)

#Câu 3
x = 10+100j
print(type(x))

#Câu 4
base = input("Enter base:")
b=float(base)
height = input("Enter height:")
h=float(height)
area=0.5 * b * h
a=int(area)
print("The area of the triangle is",a)

#Câu 5
a=input("Enter side a:")
a=float(a)
b=input("Enter side b:")
b=float(b)
c=input("Enter side c:")
c=float(c)
perimeter=a + b +c
p=int(perimeter)
print("The perimeter of the triangle is",p)

#Câu 6
lenght = input("Nhập chiều dài:")
l = float(lenght)
heght = input("Nhập chiều rộng:")
h = float(heght)
dientich = l*h
chuvi= 2 *(l+h)
print("Chu vi HCM là",chuvi)
print("Diện tích HCN là",dientich)

#Câu 7
r = input("Bán kính là")
r = float(r)
dientich=(math.pi * r *r )
chuvi = (2 *math.pi*r)
print("Diện tích",dientich)
print("Chu vi:",chuvi)

#
for n in range(1, 6):
    print(f"{n}   {n**0}    {n**1}    {n**2}    ")