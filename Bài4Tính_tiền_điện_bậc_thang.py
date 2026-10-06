tien_dien=float(input("Nhập số điện tiêu thụ kwh: "))
if tien_dien >201:
    tien_dien=tien_dien*2536
elif tien_dien >101:
    tien_dien=tien_dien*2014
elif tien_dien >51:
    tien_dien=tien_dien*1734
elif tien_dien >0:
    tien_dien=tien_dien*1678
else:
    print("Số kwh không hợp lệ")
print("Số tiền điện phải trả là:",tien_dien,"VNĐ")