#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Giá trị truyệt đối - abs()
import pdb

a = -5
print(abs(a))

#Check hàm a hoặc b có thể lặp hay không - all()
#Mục đích hàm này khi có kết quả trả về là false thì kết quả sẽ
#Kết quả 0 được coi là false, rỗng được coi là False
a = 1
b = ["v", "n", "a"]
print(all([a,b]))

#Kiểm tra có ít nhất 1 phần tử trong danh sách trả về True -> sẽ true
#Kết quả 0 được coi là false, rỗng được coi là False
c = []
print(any([a,b,c]))
"""
a -> True
b-> True
C-> 
"""

#Các ký tựu không  ascii sẽ được thay thế bằng các ký tự escape
e = "Đoàn Vũ Lê"
f = "こんにちは"
g = "Vu Le Doan"
print(ascii([e,f,g]))

#bin() Dùng để chuyển số nguyên integer thành chuỗi nhị phân Binary string
#Chuỗi nhị phân bắt đầu bằng 0b
k = 10
g = -100
print(bin(k))
print(bin(g))

#Hàm bool() -> Trả về đúng sai
a = 10
b = 11
c=bool(a>b)
print(c)

#breakpoint() đối với python 3.7 - pdb.set_trace() tương tự như  -> thường dùng để debuging nếu không truyền tham số gì vào thì đến nơi nó sẽ ngưng lại để debug
if (a>b):
        print ("True")
else:
    print ("Sai")
    #pdb.set_trace()

#bytearry() được sử dụng đẻ tạo 1 mảng byte
s = [10,11]
b = bytearray(s)
print(b)