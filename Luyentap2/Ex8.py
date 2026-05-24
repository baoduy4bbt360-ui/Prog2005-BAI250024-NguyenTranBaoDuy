# Bài 8 Yêu cầu: Nhập hai số nguyên từ bàn phím và in ra kết quả phép chia của chúng. Xử lý chia cho 0 và dữ liệu không hợp lệ\
print("Bai 8")
a= int(input("Nhap a: "))
b= int(input("Nhap b: "))
if b!=0:
    ketqua = a / b
    print(f"Ket qua la:{ketqua}")
else:
    print("Du lieu khong hop le!")
