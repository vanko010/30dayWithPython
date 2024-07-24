import difflib
import json

with open("db.json", "r", encoding='utf-8') as f:
    db = json.load(f)
db_dict = {(item['lastname'],item['firstname'],item['birthday'],item['sex'], item['phone'],item['email']): item for item in db}
print(type(db_dict))
def checkgiong(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).ratio()
timkiem = input("Nhập thông tin tìm kiếm:")
timkiem1 = timkiem.split()
timkiem1 = str(timkiem1)
for data in db_dict:
    hoten= data["lastname"]+" "+ data["firstname"]
    hoten1= hoten.split()
    hoten1=str(hoten1)
    sshovaten= checkgiong(timkiem1, hoten1)
    if sshovaten >= 0.6:
        print("Độ giống nhau của thông tin tìm kiếm:", sshovaten)
        for key, value in item.items():
            if value.strip():
                print(f"{key}:{value}")