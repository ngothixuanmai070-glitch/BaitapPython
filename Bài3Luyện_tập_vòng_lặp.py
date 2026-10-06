N=int(input("Nhập số n: "))
tong=0
for i in range(1,N+1):
    if i%10==0:
        continue
    if i%2!=0:
        tong+=i
print("Tổng các số lẻ từ 1 đến",N,"là:",tong)