#Hàm
#def person():
 #   ten = "Vu"
 #   ho = "Le"
  #  space = " "
  #  fullname = ho + space + ten
  #  return f"{ho} {ten}"
#print(person())

def timkiem():
    timten = input("Tìm tên:")
    timho = input("Tìm họ:")
    return timten, timho
timten, timho = timkiem()
print (type(timten))