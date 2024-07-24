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

def checkgiong(str1,str2):
    return difflib.SequenceMatcher(None,str1,str2).ratio()
timkiem = input("Nhập thông tin tìm kiếm:")
timkiem1 = timkiem.split()
for danhsach in db:
    hoten=danhsach["lastname"]+""+danhsach["firstname"]
    hoten1= hoten.split()
    sshovaten= checkgiong(timkiem1,hoten1)
    if sshovaten >= 0.5:
        print("Độ giống nhau của thông tin tìm kiếm:", sshovaten)
        for key,value in danhsach.items():
          if value.strip():
             print(f"{key}:{value}")