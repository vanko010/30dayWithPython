ef checkgiong(str1, str2):
#     return difflib.SequenceMatcher(None, str1, str2).ratio()
# timkiem = input("Nhập thông tin tìm kiếm:")
# timkiem1 = timkiem.split()
# timkiem1 = str(timkiem1)
# for item in db:
#     hoten= item.get("lastname")+" "+ item.get("firstname")
#     hoten1= hoten.split()
#     hoten1=str(hoten1)
#     sshovaten= checkgiong(timkiem1, hoten1)
#     if sshovaten >= 0.6:
#         print("Độ giống nhau của thông tin tìm kiếm:", sshovaten)
#         for key, value in item.items():
#             if value.strip():
#                 print(f"{key}:{value}")