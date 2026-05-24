# Bài 9 Yêu cầu: Nhập một số và tính căn bậc hai của nó. Nếu số nhập vào âm, hiển thị thông báo lỗi.
print("Bai 9")
a=int(input("Nhap a: "))
if a>=0:
    canbachai = pow(a,1/2)
    print(f"Can bac hai cua {a} la:{canbachai}")
else:
    print("Loi!")


