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
        "sex" : gioitinh,
        "phone": sdt,
        "email": email
                }
    db.append(danhsach)

print ("=================================")
def timkiem():
    timten = input("Tìm tên:")
    timho = input("Tìm họ:")
    return timten, timho
timten, timho = timkiem()

def checkgiong(str1,str2):
    return difflib.SequenceMatcher(None,str1,str2).ratio()
giongnhau = 0.3
for danhsach in db:
    ssten = checkgiong(timten,danhsach["lastname"])
    ssho = checkgiong(timho,danhsach["firstname"])
    if ssten >= giongnhau and ssho >=giongnhau:
        print("Độ giống nhau của tên:",ssten, "Họ",ssho)
        for key, value in danhsach.items():
                print(f"{key}:{value}")
                print("-------------------")