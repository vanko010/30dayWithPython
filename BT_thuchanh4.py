import difflib
import json

with open("db.json", "r", encoding='utf-8') as f:
    db = json.load(f)
def checkgiong(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).ratio()
timkiem = input("Nhập thông tin tìm kiếm:")
timkiem1 = timkiem.split()
print("====================")
db_out=[]
for data in db:
    hoten= data["lastname"]+" "+ data["firstname"]
    hoten1= hoten.split()
    sshovaten= checkgiong(timkiem1, hoten1)
    if sshovaten >= 0.5:
        print("Độ giống nhau của thông tin tìm kiếm:", sshovaten)
        record={}
        for key, value in data.items():
            if value.strip():
                print(f"{key}:{value}")
                record[key]=value
        db_out.append(record)
print(db_out)
if len(db_out)!= 0:
    with open("db_out.json", "w", encoding='utf-8') as file:
        json.dump(db_out,file,ensure_ascii=False,indent=4)
else:
    print("Không ghi file vì file rỗng")