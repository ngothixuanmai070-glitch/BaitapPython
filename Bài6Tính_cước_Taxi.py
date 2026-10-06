km=float(input("Nhập số km đi được: "))
if km<=0:
    print("Số km phải lớn hơn 0")
else:
    if km<=1:
        tien=15000
    elif km<=30:
        tien=15000+(km-1)*12000
    else:
        tien=15000+29*12000+(km-30)*10000
if km>100:
    tien*=0.9
print("Cước taxi:", f"{tien:,.0f} VNĐ")
