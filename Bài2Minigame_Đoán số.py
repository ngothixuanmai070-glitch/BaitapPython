import random
secret_number = random.randint(1, 50)
while True:
    guess = int(input("Đoán số từ 1 đến 50: "))
    if guess < secret_number:
        print("Số bạn đoán nhỏ hơn số bí mật.")
    elif guess > secret_number:
        print("Số bạn đoán lớn hơn số bí mật.")
    else:
        print("Chúc mừng! Bạn đã đoán đúng số bí mật:", secret_number)
        break