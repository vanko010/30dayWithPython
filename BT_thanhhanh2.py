import difflib
db = []
soluongdb = int(input("Nhập số lượng db muốn thêm: "))
for soluong in range(soluongdb):
    ten = input("Tên:")
    ho = input("Họ:")
    ngaysinh = input("Ngày sinh:")
    gioitinh = input("Giới tính:")
    sdt = input("Số điện thoại:")
    email = input("Email:")
    danhsach = {
        "lastname": ten,
        "firstname": ho,
        "birthday": ngaysinh,
        "sex": gioitinh,
        "phone": sdt,
        "email": email
                }
    db.append(danhsach)

print(db)
print(type(db))

# print ("=================================")
# timkiem = input("Tìm thông tin:")
# def checkgiong(str1,str2):
#     return difflib.SequenceMatcher(None,str1,str2).ratio()
# for danhsach in db:
#     hovaten = danhsach["firstname"]+" "+danhsach["lastname"]
#     tenvaho=danhsach["lastname"]+" "+danhsach["firstname"]
#     timkiem2 = checkgiong(timkiem,hovaten)
#     timkiem3= checkgiong(timkiem,tenvaho)
#     if timkiem2 >= 0.5:
#         print("Độ giống nhau của thông tin:",timkiem2)
#         for key, value in danhsach.items():
#             if value.strip():
#                 print(f"{key}:{value}")
#     if timkiem3 >= 0.5:
#         print("Độ giống nhau của thông tin:", timkiem3)
#         for key, value in danhsach.items():
#             if value.strip():
#                 print(f"{key}:{value}")
