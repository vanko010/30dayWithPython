import math
#Ngày 2: 30 ngày lập trình python
ten = 'Vu'
ho = 'Le'
tendaydu = 'Le Doan Vu'
quocgia = 'Viet Nam'
thanhpho = 'Ho Chi Minh'
tuoi = 23
nam = '2024'
is_married = 'married'
is_true = True
is_light_on = 'On'
a,b,c,d = '1','2','3','4'
print(ten)
print(ho)
print(tendaydu)
print(quocgia)
print(thanhpho)
print(tuoi)
print(nam)
print(is_married)
print(is_true)
print(is_light_on)
print(a,b,c,d)

#BT2
print(type(ten))
print(type(ho))
print(type(tendaydu))
print(type(quocgia))
print(type(thanhpho))
print(type(tuoi))
print(type(nam))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type({a,b,c,d}))

print(len(ten))

if len(ten) > len(ho):
    print("Ten dai hơn ", len(ten))
else:
    if len(ten) < len(ho):
        print("Ho dai hon", len(ho))
    else:
        print("Ten bang ho", len(ten))

num_one = 5
num_two = 4
total= num_one + num_two
print("Kết quả là",total)
diff = num_two - num_one
print("Kết quả là", abs(diff))
product = num_two * num_one
print("Kết quả là", product)
division = num_two / num_one
print("Kết quả là", division)
floor_division = num_one // num_two
print("Kết quả là", floor_division)

#Diện tích hình tròn
r = 30 #bán kính
area_of_circle = math.pi * (r**2)
print("Diện tích hình tròn", area_of_circle)

circum_of_circle = 2 * math.pi * r
print("Chu vi hình tròn",circum_of_circle)

r1 = input("Bán kính:")
r1=float(r1)
area_of_circle = math.pi * (r1**2)
print("Diện tích hình tròn", area_of_circle)

circum_of_circle = 2 * math.pi * r1
print("Chu vi hình tròn",circum_of_circle)

ten = input("Nhập Tên:")
ho = input("Nhập Họ:")
quocgia = input("Nhập quốc gia:")
age = input("Nhập tuổi:")
print(f"Tên: {ten}")
print(f"Họ: {ho}")
print(f"Quốc gia: {quocgia}")
print(f"Tuổi: {age}")